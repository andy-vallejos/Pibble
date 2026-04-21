import os
from io import BytesIO

import magic
import PIL.Image
import requests
from dotenv import load_dotenv
from google import genai
from google.genai import errors, types


class AIClient:
    def __init__(self):
        self._cliente = None
        self._modelo = None
        self._iniciado = False

    def get_cliente(self):
        return self._cliente

    def get_modelo(self):
        return self._modelo

    def iniciar(self):
        if not self._iniciado:
            load_dotenv()
            api_key = os.getenv("GOOGLE_API_KEY")
            if not api_key:
                raise ValueError("Falta GOOGLE_API_KEY en el .env")

            self._cliente = genai.Client(api_key=api_key)

            models = list(self._cliente.models.list())
            self._modelo = next(
                (m.name for m in models if "flash" in m.name.lower()), models[0].name
            )

            self._iniciado = True

    def _obtener_recurso(self, ruta_o_url):
        if ruta_o_url.startswith(("http://", "https://")):
            try:
                res = requests.get(ruta_o_url, timeout=10)
                res.raise_for_status()
                datos = res.content
                mime = magic.from_buffer(datos, mime=True)
                return datos, mime
            except Exception as e:
                raise RuntimeError(f"Error al descargar URL: {e}")
        else:
            if not os.path.exists(ruta_o_url):
                raise FileNotFoundError(f"No existe el archivo: {ruta_o_url}")

            with open(ruta_o_url, "rb") as f:
                datos = f.read()

            mime = magic.from_file(ruta_o_url, mime=True)
            return datos, mime

    def generar_respuesta(self, prompt: str, archivos: list = None):
        if not self._iniciado:
            self.iniciar()

        contenido = [prompt]

        if archivos:
            for ruta in archivos:
                try:
                    datos, mime = self._obtener_recurso(ruta)

                    if mime.startswith("image"):
                        img = PIL.Image.open(BytesIO(datos))
                        contenido.append(img)

                    elif mime.startswith("audio"):
                        contenido.append(
                            types.Part.from_bytes(data=datos, mime_type=mime)
                        )

                    else:
                        print(f"Formato no soportado omitido: { mime }")

                except Exception as e:
                    print(f"Error procesando { ruta }: { e }")

        try:
            res = self._cliente.models.generate_content(
                model=self._modelo, contents=contenido
            )
            return {
                "texto": res.text,
                "tokens": res.usage_metadata.total_token_count,
                "estado": "success",
                "objeto_orginal": res,
            }
        except errors.ClientError:
            return {"texto": "Error de cuota o cliente API.", "estado": "error"}
        except Exception as e:
            return {"texto": f"Error crítico: {e}", "estado": "error"}
