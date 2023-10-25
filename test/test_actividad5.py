import pytest
from src.actividad5 import verificar_contraseña
@pytest.mark.parametrize(
    "contraseñausuario, mensaje",
    [
        ("us", "contraseña incorrecta, intentalo de nuevo: "),
        ("us", "Incorrect Password!!")


    ]      
)
def test_verificar_contraseña_params(contraseñausuario,mensaje):
    assert verificar_contraseña(contraseñausuario) == mensaje
def test_verificar_contraseña_params():
    with pytest.raises(NameError):
        verificar_contraseña("us")=="Incorrect Password!!"