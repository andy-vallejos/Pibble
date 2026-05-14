from src.gramatica import *
from src.ia import *
from src.audio import *

texto = """
Hola hola mundo.
Mi correo es andyvallejosgb@gmail.com
Visita https://google.com
Tengo 22
"""

print(texto)

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

print("Validacion con reglas")

resultado_validacion = validar(texto, [
    empieza_en_mayuscula,
    termina_con_puntuacion,
    tiene_minusculas
])

print(resultado_validacion)

print()


print("=== Extraccion con reglas ===")

resultado_extraccion = extraer(texto, [
    buscar_email,
    buscar_url,
    buscar_numero_celular
])

print(resultado_extraccion)

print()
print("=== Extraccion con IA ===")

resultado_ia = extraer_ia(
    texto,
    "correos electrónicos y números telefónicos"
)

print(resultado_ia)

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
    "Que se ve en la imagen",
    ["https://imgs.search.brave.com/2fGJ6LnNalx0rWaCFfhzvnRxWVhEpFdBax1iW_i5JFM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly90NC5m/dGNkbi5uZXQvanBn/LzA2Lzg5LzM5LzAx/LzM2MF9GXzY4OTM5/MDExMV9qRjRqVXdx/UG5VUDNscEhlRE8y/aXRWa1NydEJ4WXVv/di5qcGc"]
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
