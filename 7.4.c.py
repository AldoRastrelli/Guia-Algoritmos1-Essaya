# vector :: tupla (para trabajar con elemento inmutables).

def son_paralelos(tupla1,tupla2):
    "indica si los vectores son paralelos"

    div = int(tupla1[0]) / int(tupla2[0])
    for i in range(1,len(tupla1)):  # [1,2) entonces i =1
        if div == int(tupla1[i]) / int(tupla2[i]):
            continue
        else:
            return False
    return True

def solcitar_tuplas_igual_dimension():
    "solicita tuplas de igual dimensión al usuario"
    
    tupla1 = input("Ingrese un vector: ").split(" ")
    tupla2 = input("Ingrese un vector: ").split(" ")

    while not verificar_dimension(tupla1,tupla2):
        print("Los vectores no tienen la misma dimensión")
        tupla1 = input("Ingrese un nuevo vector: ").split(" ")
        tupla2 = input("Ingrese un nuevo vector: ").split(" ")

    return (tuple(tupla1),tuple(tupla2))

def verificar_dimension(tupla1,tupla2):
    "verifica que ambas tuplas tengan la misma dimensión"

    return len(tupla1) == len(tupla2)

print("El programa indica si dos vectores son paralelos entre sí")
tupla1, tupla2 = solcitar_tuplas_igual_dimension()
print(son_paralelos(tupla1,tupla2))