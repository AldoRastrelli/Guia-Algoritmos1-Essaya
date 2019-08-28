import math

def solicitar_lista_de_enteros():
    "solicita una lista con números enteros al usuario"
    
    lista = input("Ingrese una lista con números enteros: ").split(" ")

    while not verificar_enteros_positivos(lista):
        print("Los elementos deben ser numeros naturales.")
        lista = input("Ingrese una nueva lista: ").split(" ")

    return lista

def verificar_enteros_positivos(lista):
    "verifica que la lista tenga sólo números enteros"

    for x in lista:
        if not x.isdigit():
            return False
        continue
    return True

def lista_factorial(lista):
    "devuelve el factorial de cada elemento"

    for i in range(len(lista)):
        lista[i] = math.factorial(int(lista[i]))
    return lista
      
print("El programa devuelve el factorial de cada elemento de la lista.\nLos elementos deben ser numeros naturales.")
lista = solicitar_lista_de_enteros()
print(lista_factorial(lista))