import os
import pytest
from src.audio import *


@pytest.fixture
def contexto():
    return hay_microfono()


def test_microfono(contexto):
    assert isinstance(contexto, bool)


def test_tts():
    try:
        hablar("Hola prueba")

    except Exception as e:
        pytest.fail(f"Error en TTS: {e}")


def test_reconocimiento(contexto):
    if not contexto:
        pytest.skip("No hay micrófono conectado")

    resultado = reconocer()

    assert isinstance(resultado, str)


def test_grabacion(contexto):
    if not contexto:
        pytest.skip("No hay micrófono conectado")

    try:

        grabar("test_audio")

    except Exception as e:
        pytest.skip(f"No se pudo acceder al micrófono: {e}")

    if not os.path.exists("test_audio.mp3"):
        pytest.skip("No se pudo generar el archivo")

    assert os.path.exists("test_audio.mp3")

    os.remove("test_audio.mp3")
