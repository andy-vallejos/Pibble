import re
import os
from google import genai

def cargar_vocabulario(ruta_archivo):
    try:
        if ruta_archivo and os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return {linea.strip().lower() for linea in archivo if linea.strip()}
    except Exception:
        pass
    return {"proyecto", "clase", "sistema", "informática", "universidad"}

def calcular_diferencia_letras(palabra_a, palabra_b):
    if len(palabra_a) < len(palabra_b): 
        return calcular_diferencia_letras(palabra_b, palabra_a)
    if len(palabra_b) == 0: 
        return len(palabra_a)
    
    fila_anterior = range(len(palabra_b) + 1)
    for i, letra_a in enumerate(palabra_a):
        fila_actual = [i + 1]
        for j, letra_b in enumerate(palabra_b):
            sustitucion = fila_anterior[j] + (letra_a != letra_b)
            fila_actual.append(min(fila_anterior[j+1] + 1, fila_actual[j] + 1, sustitucion))
        fila_anterior = fila_actual
    return fila_anterior[-1]

def corregir_palabra_local(palabra, diccionario, nombres_propios):
    palabra_limpia = palabra.lower().strip(",.?!")
    
    for nombre in nombres_propios:
        if palabra_limpia == nombre.lower():
            return nombre
    
    if palabra_limpia in diccionario:
        return palabra_limpia
    
    if len(palabra_limpia) > 3:
        for palabra_correcta in diccionario:
            if palabra_correcta.startswith(palabra_limpia[0]):
                if calcular_diferencia_letras(palabra_limpia, palabra_correcta) == 1:
                    return palabra_correcta
    
    return palabra_limpia

def solicitar_refinamiento_ia(cliente_ia, modelo_ia, texto_sucio):
    instrucciones = (
        "Actúa como corrector gramatical técnico. "
        "Corrige puntuación y coherencia del siguiente texto derivado de audio. "
        "No añadas explicaciones, solo devuelve el texto corregido: "
    )
    
    try:
        respuesta = cliente_ia.models.generate_content(
            model=modelo_ia,
            contents=f"{instrucciones} {texto_sucio}"
        )
        return respuesta.text.strip()
    except Exception:
        return texto_sucio

def ejecutar_limpieza_hibrida(ruta_txt, api_key, nombres, sonidos):
    if not os.path.exists(ruta_txt):
        return None

    cliente = genai.Client(api_key=api_key)
    modelo = "gemini-2.0-flash" 
    diccionario = cargar_vocabulario("diccionario.txt")

    with open(ruta_txt, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    contenido_final = []
    
    for linea in lineas:
        linea_previa = linea
        for sonido in sonidos:
            linea_previa = re.sub(sonido, '', linea_previa, flags=re.IGNORECASE)
        
        palabras = linea_previa.split()
        palabras_corregidas = [corregir_palabra_local(p, diccionario, nombres) for p in palabras]
        texto_pre_pulido = " ".join(palabras_corregidas)

        if len(texto_pre_pulido.strip()) > 0:
            resultado_optimo = solicitar_refinamiento_ia(cliente, modelo, texto_pre_pulido)
            
            oracion = resultado_optimo.capitalize()
            if not oracion.endswith(('.', '!', '?')): 
                oracion += "."
            contenido_final.append(oracion)

    ruta_salida = ruta_txt.replace(".txt", "_optimo.txt")
    with open(ruta_salida, 'w', encoding='utf-8') as archivo_final:
        archivo_final.write("\n".join(contenido_final))
    
    return ruta_salida