import pytest
from src.actividad1 import crear_lista
@pytest.mark.parametrize(
    "edad, lista",
    [
        (21,"1 años cumplidos\n2 años cumplidos\n3 años cumplidos\n4 años cumplidos\n5 años cumplidos\n6 años cumplidos\n7 años cumplidos\n8 años cumplidos\n9 años cumplidos\n10 años cumplidos\n11 años cumplidos\n12 años cumplidos\n13 años cumplidos\n14 años cumplidos\n15 años cumplidos\n16 años cumplidos\n17 años cumplidos\n18 años cumplidos\n19 años cumplidos\n20 años cumplidos\n21 años cumplidos\n"),
        (-1,": no se permiten numeros negativos"),
    ]   
)
def test_crear_lista_params(edad,lista):
    assert crear_lista(edad) == lista

def test_crear_lista_params():
    with pytest.raises(ValueError):
        crear_lista(-1)==": no se permiten numeros negativos"