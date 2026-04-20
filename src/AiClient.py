import os
from dotenv import load_dotenv
from google import genai


class AIClient:
    def __init__(self):
        self._cliente = None
        self._modelo = None
        self._iniciado = False

    def iniciar(self):
        if self._iniciado:
            return self._cliente, self._modelo

        load_dotenv()

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("No se encontró GOOGLE_API_KEY")

        self._cliente = genai.Client(api_key=api_key)

        models = list(self._cliente.models.list())
        if not models:
            raise RuntimeError("No hay modelos disponibles")

        self._modelo = next(
            (m.name for m in models if "flash" in m.name.lower()),
            models[0].name
        )

        self._iniciado = True

        return self._cliente, self._modelo

    def generar(self, prompt):
        if not self._iniciado:
            self.iniciar()

        return self._cliente.models.generate_content(
            model=self._modelo,
            contents=prompt
        )
