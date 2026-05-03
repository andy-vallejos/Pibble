import os
import pytest
from src.audio import grabar


@pytest.fixture
def contexto():
    prueba = "prueba"
    tiempo = 2

    return prueba, tiempo


def test_creacion_archivo_final(contexto):
    prueba, tiempo = contexto
    grabar(prueba, tiempo)
    archivo_creado = f"{prueba}.mp3"
    existe = os.path.exists(archivo_creado)
    assert existe == True
    if existe:
        os.remove(archivo_creado)


def test_eliminar_archivo_wav(contexto):
    prueba, tiempo = contexto
    grabar(prueba, tiempo)
    archivo_mp3 = f"{prueba}.mp3"
    archivo_wav = f"{prueba}.wav"
    assert os.path.exists(archivo_mp3) == True
    assert os.path.exists(archivo_wav) == False
    os.remove(archivo_mp3)
