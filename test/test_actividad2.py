import pytest
from src.actividad2 import crear_impares
@pytest.mark.parametrize(
    "numero, impares",
    [
        (21,"1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21"),
        (-1,": solo se permiten numeros mayores que cero")
    ]  
)
def test_crear_impares_params(numero, impares):
    assert crear_impares(numero) == impares
def test_crear_impares_params():
    with pytest.raises(ValueError):
        crear_impares(-1)==": solo se permiten numeros mayores que cero"