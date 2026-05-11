import os
import pyttsx3
import sounddevice as sd
import soundfile as sf
import numpy as np
import speech_recognition as sr
from pydub import AudioSegment

engine = pyttsx3.init()


def hablar(texto):
    try:
        engine.say(texto)
        engine.runAndWait()

    except Exception as e:
        print(f"[ERROR TTS]: {e}")


def hay_microfono():
    try:
        dispositivos = sd.query_devices()

        for d in dispositivos:
            if d["max_input_channels"] > 0:
                return True

        return False

    except Exception:
        return False


def reconocer():
    if not hay_microfono():
        return "No hay micrófono conectado"

    reconocedor = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("Habla ahora...")
            print("Presiona Ctrl+C para finalizar")

            reconocedor.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio_data = []

            while True:
                try:
                    audio = reconocedor.listen(
                        source,
                        timeout=2,
                        phrase_time_limit=5
                    )

                    audio_data.append(audio)

                except sr.WaitTimeoutError:
                    continue

    except KeyboardInterrupt:
        print("\nFinalizando grabación...")

    except Exception as e:
        return f"Error con micrófono: {e}"

    if not audio_data:
        return "No se capturó audio"

    try:

        raw_data = b"".join(
            [a.get_raw_data() for a in audio_data]
        )

        audio_completo = sr.AudioData(
            raw_data,
            audio_data[0].sample_rate,
            audio_data[0].sample_width
        )

        texto = reconocedor.recognize_google(
            audio_completo,
            language="es-ES"
        )

        return texto

    except sr.UnknownValueError:
        return "No se entendió el audio"

    except sr.RequestError:
        return "Error con el servicio de reconocimiento"

    except Exception as e:
        return f"Error: {e}"


def grabar(nombre_archivo):
    if not hay_microfono():
        print("No hay micrófono conectado")
        return

    frecuencia = 44100
    canales = 1

    print("Grabando...")
    print("Presiona Ctrl+C para finalizar")

    frames = []

    try:

        stream = sd.InputStream(
            samplerate=frecuencia,
            channels=canales,
            dtype='int16'
        )

        stream.start()

        while True:

            data, overflowed = stream.read(1024)

            if overflowed:
                print("Overflow detectado")

            frames.append(data)

    except KeyboardInterrupt:
        print("\nFinalizando grabación...")

    except Exception as e:
        print(f"Error grabando: {e}")
        return

    finally:
        try:
            stream.stop()
            stream.close()
        except:
            pass

    if not frames:
        print("No se grabó audio")
        return

    try:

        grabacion = np.concatenate(frames, axis=0)

        archivo_wav = nombre_archivo + ".wav"

        sf.write(
            archivo_wav,
            grabacion,
            frecuencia
        )

        audio_segment = AudioSegment.from_wav(
            archivo_wav
        )

        archivo_mp3 = nombre_archivo + ".mp3"

        audio_segment.export(
            archivo_mp3,
            format="mp3"
        )

        os.remove(archivo_wav)

        print("Grabación terminada")

    except Exception as e:
        print(f"Error procesando audio: {e}")
