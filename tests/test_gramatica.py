import pytest
from src.gramatica import *


def test_esta_vacio():
    assert esta_vacio("   ") is True
    assert esta_vacio("Hola") is False


def test_tiene_numeros():
    assert tiene_numeros("abc123") is True
    assert tiene_numeros("hola") is False


def test_tiene_caracteres_especiales():
    assert tiene_caracteres_especiales("hola@") is True
    assert tiene_caracteres_especiales("Hola Mundo") is False


def test_es_solo_letras():
    assert es_solo_letras("Hola Mundo") is True
    assert es_solo_letras("Hola123") is False


def test_tiene_mayusculas():
    assert tiene_mayusculas("Hola") is True
    assert tiene_mayusculas("hola") is False


def test_tiene_minusculas():
    assert tiene_minusculas("Hola") is True
    assert tiene_minusculas("HOLA") is False


def test_contar_palabras():
    assert contar_palabras("Hola mundo cruel") == 3


def test_contar_oraciones():
    assert contar_oraciones("Hola. Como estas? Bien!") == 3


def test_contar_caracteres():
    assert contar_caracteres("Hola") == 4


def test_empieza_en_mayuscula():
    assert empieza_en_mayuscula("Hola") is True
    assert empieza_en_mayuscula("hola") is False


def test_termina_con_puntuacion():
    assert termina_con_puntuacion("Hola.") is True
    assert termina_con_puntuacion("Hola") is False


def test_doble_espaciado():
    assert doble_espaciado("Hola  mundo") is True
    assert doble_espaciado("Hola mundo") is False


def test_palabras_repetidas():
    assert palabras_repetidas("hola hola") is True
    assert palabras_repetidas("hola mundo") is False


def test_verificar_estructura_basica_valido():
    resultado = verificar_estructura_basica("Hola mundo.")

    assert resultado["valido"] is True
    assert resultado["errores"] == []


def test_verificar_estructura_basica_invalido():
    resultado = verificar_estructura_basica("hola  hola")

    assert resultado["valido"] is False
    assert len(resultado["errores"]) > 0


def test_buscar_email():
    resultado = buscar_email("Mi correo es test@gmail.com")

    assert resultado == ["test@gmail.com"]


def test_buscar_url():
    resultado = buscar_url("Visita https://google.com")

    assert resultado == ["https://google.com"]


def test_buscar_numero_celular():
    resultado = buscar_numero_celular("Mi numero es +591 77777777")

    assert resultado == ["+591 77777777"]


def test_buscar_fechas():
    resultado = buscar_fechas("La fecha es 10/05/2026")

    assert resultado == ["10/05/2026"]


def test_remover_espacios_extra():
    resultado = remover_espacios_extra("Hola    mundo")

    assert resultado == "Hola mundo"


def test_remover_caracteres_especiales():
    resultado = remover_caracteres_especiales("Hola@123!")

    assert resultado == "Hola"


def test_normalizar_texto():
    resultado = normalizar_texto("HÓLÁ   MUNDO")

    assert resultado == "hola mundo"


def test_tokenizar_palabras():
    resultado = tokenizar_palabras("Hola mundo cruel")

    assert resultado == ["Hola", "mundo", "cruel"]


def test_tokenizar_oraciones():
    resultado = tokenizar_oraciones("Hola. Como estas? Bien!")

    assert resultado == [
        "Hola.",
        "Como estas?",
        "Bien!"
    ]


def test_obtener_palabras_mas_comunes():
    resultado = obtener_palabras_mas_comunes(
        "hola hola mundo"
    )

    assert resultado[0] == ("hola", 2)


def test_riqueza_lexica():
    resultado = riqueza_lexica("hola hola mundo")

    assert resultado == 2 / 3


def test_puntaje_legibilidad():
    resultado = puntaje_legibilidad(
        "Hola mundo. Como estas."
    )

    assert resultado == 2


def regla_con_numero(texto):
    return tiene_numeros(texto)


def regla_mayuscula(texto):
    return tiene_mayusculas(texto)


def test_validar_valido():
    resultado = validar(
        "Hola123",
        [regla_con_numero, regla_mayuscula]
    )

    assert resultado["valid"] is True


def test_validar_invalido():
    resultado = validar(
        "hola",
        [regla_con_numero, regla_mayuscula]
    )

    assert resultado["valid"] is False
    assert len(resultado["errores"]) == 2


def test_coincide_regla():
    assert coincide_regla(
        "hola123",
        r"\d+"
    ) is True

    assert coincide_regla(
        "hola",
        r"\d+"
    ) is False
