import pytest
from src.ia import inicializar, generar_respuesta


@pytest.fixture
def contexto():
    cliente, modelo = inicializar()
    return cliente, modelo


def test_inicializacion(contexto):
    cliente, modelo = contexto
    assert cliente is not None
    assert modelo is not None


def test_modelo_valido(contexto):
    _, modelo = contexto
    assert len(modelo) > 0


def test_generar_respuesta(contexto):
    cliente, modelo = contexto
    respuesta = generar_respuesta(cliente, modelo, "Dime algo")
    assert isinstance(respuesta, dict)
