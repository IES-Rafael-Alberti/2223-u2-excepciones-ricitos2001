import pytest
from src.actividad4 import verificar_numero
@pytest.mark.parametrize(
    "numero, mensaje",
    [
        (1," es un numero entero"),
        (-1," es un numero entero"),
        (1.0," no es un numero entero"),
        ("a"," no es un numero entero"),
        ("A"," no es un numero entero")


    ]   
)
def test_verificar_numero_params(numero,mensaje):
    assert verificar_numero(numero) == mensaje
    assert verificar_numero(numero) == mensaje
def test_verificar_numero_params():
    with pytest.raises(ValueError):
        verificar_numero("1.0")==" no es un numero entero"
        verificar_numero("a")==" no es un numero entero"
        verificar_numero("A")==" no es un numero entero"