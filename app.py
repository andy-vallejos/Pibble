from src.gramatica import *
from src.ia import *
from src.audio import *

texto = """
Hola hola mundo.
Mi correo es andyvallejosgb@gmail.com
Visita https://google.com
"""

print("=== ANALISIS DE TEXTO ===")

print("Texto vacio:", esta_vacio(texto))
print("Tiene numeros:", tiene_numeros(texto))
print("Tiene mayusculas:", tiene_mayusculas(texto))
print("Cantidad de palabras:", contar_palabras(texto))
print("Cantidad de oraciones:", contar_oraciones(texto))
print("Cantidad de caracteres:", contar_caracteres(texto))
print("Palabras repetidas:", palabras_repetidas(texto))
print("Empieza en mayuscula:", empieza_en_mayuscula(texto))
print("Termina con puntuacion:", termina_con_puntuacion(texto))

print()

print("=== EXTRACCION DE DATOS ===")

print("Emails encontrados:")
print(buscar_email(texto))

print()

print("URLs encontradas:")
print(buscar_url(texto))

print()

print("=== TOKENIZACION ===")

print("Palabras:")
print(tokenizar_palabras(texto))

print()

print("Oraciones:")
print(tokenizar_oraciones(texto))

print()

print("=== ESTADISTICAS ===")

print("Palabras mas comunes:")
print(obtener_palabras_mas_comunes(texto))

print()

print("Riqueza lexica:")
print(riqueza_lexica(texto))

print()

print("Puntaje de legibilidad:")
print(puntaje_legibilidad(texto))

print()

print("=== VALIDACION ===")

reglas = [
    tiene_mayusculas,
    termina_con_puntuacion
]

resultado_validacion = validar(texto, reglas)

print(resultado_validacion)

print()

print("=== REGEX PERSONALIZADA ===")

print(
    coincide_regla(
        texto,
        r"\bcorreo\b"
    )
)

print()

print("=== NORMALIZACION ===")

texto_normalizado = normalizar_texto(texto)

print(texto_normalizado)

print()

print("=== IA GEMINI ===")

cliente, modelo = inicializar()

respuesta = generar_respuesta(
    cliente,
    modelo,
    "Que es esta imagen",
    ["https://unsplash.com/s/photos/hachiko"]
)

print("Estado:")
print(respuesta["estado"])

print()

print("Respuesta IA:")
print(respuesta["texto"])

print()

print("Tokens usados:")
print(respuesta.get("tokens"))

print()

print("Errores:")
print(respuesta["errores"])

print()

print("=== VOZ A TEXTO ===")

hablar("Habla ahora y presiona enter para terminar.")

texto_voz = reconocer()

print("Texto reconocido:")
print(texto_voz)
