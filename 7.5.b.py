def solicitar_lista_de_enteros():
    "solicita una lista con números enteros al usuario"
    
    lista = input("Ingrese una lista con números enteros: ").split(" ")

    while not verificar_enteros(lista):
        print("La lista debe tener únicamente números enteros.")
        lista = input("Ingrese una nueva lista: ").split(" ")

    return lista

def verificar_enteros(lista):
    "verifica que la lista tenga sólo números enteros"

    for x in lista:
        if not x.isdigit():
            if x != "" and x[0] == "-" and x[1:].isdigit():
                continue
            else:
                return False
        continue
    return True

def suma_y_promedio(lista):
    "devuelve la suma y el promedio de los elementos de la lista"

    suma = 0
    for elem in lista:
        suma += int(elem)
    promedio = suma / len(lista)

    return suma,promedio
      
print("El programa devuelve la suma y el promedio de los elementos de la lista.")
lista = solicitar_lista_de_enteros()
print(suma_y_promedio(lista))