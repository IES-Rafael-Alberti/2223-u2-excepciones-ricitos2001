import pytest
from src.actividad3 import crear_lista
@pytest.mark.parametrize(
    "numero, lista",
    [
        (21,"21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0"),
        (1.0,": solo se permiten valores numericos mayores a 0. intentalo de nuevo: "),
        ("c",": solo se permiten valores numericos mayores a 0. intentalo de nuevo: ")
    ]  
)
def test_crear_lista_params(numero,lista):
    assert crear_lista(numero) == lista
def test_crear_lista_params():
    with pytest.raises(ValueError):
        crear_lista("c")==": solo se permiten valores numericos mayores a 0. intentalo de nuevo: "
        crear_lista(1.0)==": solo se permiten valores numericos mayores a 0. intentalo de nuevo: "


