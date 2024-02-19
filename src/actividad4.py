'''Ejercicio 2.3.4: Escribir un programa que pida al usuario un número entero, si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta" y lanzará la excepción capturada.'''
# definicion de la funcion
def verificar_numero(numero):
    if numero==int(numero):
        mensaje=str(numero)+" es un numero entero"
        return mensaje
    else:
        raise ValueError(str(numero)+" no es un numero entero")

if __name__ == '__main__':
    numero = ''
    try:
        # entrada
        numero=input("introduce un numero: ")
        verificacion=int(numero)
        # procesamiento
        mensaje=verificar_numero(verificacion)
        # salida
        print (mensaje)
    except ValueError:
        print (str(numero)+" no es un numero entero")