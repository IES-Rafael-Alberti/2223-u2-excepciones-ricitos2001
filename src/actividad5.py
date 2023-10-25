'''Ejercicio 2.3.5: Escribir que solicite una contraseña, y si no coincide con la que se tiene, lance la excepción NameError con el mensaje, "Incorrect Password!!"'''
# definicon de la funcion
def verificar_contraseña(contraseñausuario):
    contraseña="usuario"
    mensaje="contraseña correcta"
    if contraseñausuario==contraseña:
        return mensaje
    else:
        if contraseñausuario not in [contraseña]:
            raise NameError ("Incorrect Password!!")

if __name__ == "__main__":
    try:
        # Entrada
        contraseñausuario = input("Introduce la contraseña: ")
        # procesamiento
        mensaje=verificar_contraseña(contraseñausuario)
        # salida
        print(mensaje)
    except NameError:
        print ("Incorrect Password!!")

    
