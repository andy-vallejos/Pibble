import pyttsx3
from pydub import AudioSegment
import os
import numpy as np
import sounddevice as sd
import soundfile as sf


def talk(text):
<<<<<<< desarrollo-Gramatica
    hablar = pyttsx3.init()
    voz = hablar.getProperty('voices')
    hablar.setProperty('voice', voz[0].id)
    hablar.say(text)
    hablar.runAndWait()


def grabar(nombre_archivo, tiempo):
    frec = 44100
    canales = 1

    print("grabando...")
    grabacion = sd.rec(int(tiempo*frec), samplerate=frec,
                       channels=canales, dtype='int16')
    sd.wait()
    print("grabacion terminada")
    wab = nombre_archivo + ".wav"
    sf.write(wab, grabacion, frec)
    audio_segment = AudioSegment.from_wav(wab)
    arc_mp3 = nombre_archivo+".mp3"
    audio_segment.export(arc_mp3, format="mp3")
    os.remove(wab)


def run():
    talk("que titulo tendra el audio?")
    titulo = input("ingresa el título")
    talk("que tiempo durara la grabacion?")
    tiempo = int(input("ingresa el tiempo"))
    talk("puedes comenzar a hablar")
    grabar(titulo, tiempo)
    talk("la grabacion ha terminado")


if __name__ == "__main__":
    run()
=======
    hablar.say(text)
    hablar.runAndWait() 

    hablar=pyttsx3.init()
    voz=hablar.getProperty('voices')
    hablar.setProperty('voice', voz[0].id)
 


def grabar(nombre_archivo, tiempo):
    frec=44100
    canales=1

    print("grabando...")
    grabacion=sd.rec(int(tiempo*frec),samplerate=frec,channels=canales,dtype='int16')
    sd.wait()
    print("grabacion terminada")
    wab=nombre_archivo + ".wav"
    sf.write(wab, grabacion, frec)
    audio_segment=AudioSegment.from_wav(wab)
    arc_mp3=nombre_archivo+".mp3"
    audio_segment.export(arc_mp3, format="mp3")
    os.remove(wab)

def run():
    talk("que titulo tendra el audio?")
    titulo=input("ingresa el título")
    talk("que tiempo durara la grabacion?")
    tiempo=int(input("ingresa el tiempo"))
    talk("puedes comenzar a hablar")
    grabar(titulo,tiempo)
    talk("la grabacion ha terminado")

if __name__ == "__main__":
    run()
>>>>>>> main
