'''Ejercicio 2.3.2: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.'''
# definicion de la funcion
def crear_impares(numero):
    impares = ""
    if numero > 0:
        for i in range(1, numero + 1, 2):
            impares += str(i)
            if i < numero - 1:
                impares += ", "
        return impares
    else:
        raise ValueError (str(numero)+": solo se permiten numeros mayores que cero")

if __name__=="__main__":
    try:
        # entrada
        numero = int(input("introduce un numero: "))
        # procesamiento
        impares=crear_impares(numero)
        # salida
        print(impares)
    except ValueError:
        print (str(numero)+": solo se permiten numeros mayores que cero")

