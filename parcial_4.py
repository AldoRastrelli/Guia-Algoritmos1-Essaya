"""2) Escribir un programa que pida al usuario que ingrese un total de 16 n ́umeros, y luego
los imprima en 4 columnas y 4 filas."""

def matriz_4_4(lista):
    "recibe una lista de 16 elementos y lo reorganiza en una matriz de 4 x 4"

    cont = 1
    fila = []
    matriz = []
    while cont <= 4:
        for i in range(4):
            fila.append(lista.pop(0))
        matriz.append(list(fila))
        fila = []
        cont += 1
    
    print("\n Matriz:")
    for elem in matriz:
        print(elem)

def solicitar_datos_para_lista():
    "solicita datos al usuario para ingresarlos en una lista"

    cont = 1
    lista = []
    while cont <=16:
        lista.append(input("Ingrese un número : "))
        cont += 1

    print(lista)
    return lista

lista = solicitar_datos_para_lista()
matriz_4_4(lista)