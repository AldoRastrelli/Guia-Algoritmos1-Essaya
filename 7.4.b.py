# vector :: tupla (para trabajar con elemento inmutables).

def producto_vectorial(tupla1,tupla2):
    """recibe dos tuplas y devuelve el producto vectorial entre sí"""

    res = 0
    for i in range(len(tupla1)):
        res += int(tupla1[i]) * int(tupla2[i])
    return res

def son_ortogonales(tupla1,tupla2):
    "indica si los vectores son ortogonales"

    return producto_vectorial(tupla1,tupla2) == 0

def solcitar_tuplas_igual_dimension():
    "solicita tuplas de igual dimensión al usuario"
    
    tupla1 = input("Ingrese un vector: ").split(" ")
    tupla2 = input("Ingrese un vector: ").split(" ")

    while not verificar_dimension(tupla1,tupla2):
        print("Los vectores no tienen la misma dimensión")
        tupla1 = input("Ingrese un nuevo vector: ").split(" ")
        tupla2 = input("Ingrese un nuevo vector: ").split(" ")

    return tuple(tupla1),tuple(tupla2)

def verificar_dimension(tupla1,tupla2):
    "verifica que ambas tuplas tengan la misma dimensión"

    return len(tupla1) == len(tupla2)

print("El programa indica si dos vectores son ortogonales entre sí")
tupla1, tupla2 = solcitar_tuplas_igual_dimension()
print(son_ortogonales(tupla1,tupla2))