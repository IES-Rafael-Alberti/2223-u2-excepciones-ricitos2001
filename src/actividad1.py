'''Ejercicio 2.3.1: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''
# definicion de la funcion
def crear_lista(edad):
    lista = ""
    if edad > 0:
        for i in range(edad):
            lista += str(i+1)+" años cumplidos"+"\n"
        return lista
    else:
        raise ValueError (str(edad)+": no se permiten numeros negativos")
    
if __name__=="__main__":
    try:
        # entrada
        edad = int(input("introduce tu edad: "))
        # procesamiento
        lista=crear_lista(edad)
        # salida
        print(lista)
    except ValueError:
        print (str(edad)+": no se permiten numeros negativos")