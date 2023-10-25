'''Ejercicio 2.3.3: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Deberá solicitar el número hasta introducir uno correcto.'''
# definicion de la funcion
def crear_lista(numero):
    lista=""
    verificacion=int(numero)
    if verificacion > 0:
        for i in range(numero+1):
            lista += str(numero-i)
            if i < numero:
                lista += ", "
        return lista
    raise ValueError (str(numero)+": solo se permiten valores numericos mayores a 0. intentalo de nuevo: ")

if __name__=="__main__":
    # entrada
    numero = 'error'
    while numero == 'error':
        try:
            numero = int(input("introduce un numero que no sea negativo: "))
            # procesamiento
            lista=crear_lista(numero)
            # salida
            print(lista)
        except ValueError:
            print(str(numero)+": solo se permiten valores numericos mayores a 0. intentalo de nuevo: ")
