import os
import pytest
from src.audio import grabar 

def test_creacion_archivo_final():
    prueba_1="prueba1"
    tiempo1=2
    grabar(prueba_1, tiempo1)
    archivo_creado=f"{prueba_1}.mp3"
    existe=os.path.exists(archivo_creado)
    assert existe==True
    if existe:
        os.remove(archivo_creado)
    

def test_eliminar_archivo_wav():
    prueba_2="prueba2"
    tiempo2=2
    grabar(prueba_2, tiempo2)
    archivo_mp3=f"{prueba_2}.mp3"
    archivo_wav=f"{prueba_2}.wav"
    assert os.path.exists(archivo_mp3)==True
    assert os.path.exists(archivo_wav)==False
    os.remove(archivo_mp3)

