# vector :: tupla (para trabajar con elemento inmutables).

def norma(tupla):
    "devuelve la norma de un vector"

    res = 0
    for i in range(len(tupla)):
        res += int(tupla[i])**2
    
    return (res**0.5)

def solcitar_tupla():
    "solicita una tupla"
    
    return tuple(input("Ingrese un vector: ").split(" "))

print("El programa devuelve la norma del vector.")
tupla1 = solcitar_tupla()
print(norma(tupla1))