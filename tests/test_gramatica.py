import pytest
from src.gramatica import ejecutar_limpieza_hibrida


@pytest.fixture
def contexto(tmp_path):
    archivo = tmp_path / "entrada.txt"
    archivo.write_text(
        "ehh holaa mndo\numm esto es un pryecto", encoding="utf-8")
    nombres = ["Juan", "Maria", "Pedro"]
    sonidos = ["ehh", "umm", "mmm", "este", "aaa"]

    return str(archivo), nombres, sonidos


def test_limpieza(contexto):
    ruta, nombres, sonidos = contexto

    resultado = ejecutar_limpieza_hibrida(
        ruta_txt=ruta,
        nombres=nombres,
        sonidos=sonidos
    )

    assert resultado is not None
    assert isinstance(resultado, str)
    assert resultado.endswith("_optimo.txt")
