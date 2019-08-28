def es_potencia_de_dos(n):
    """recibe un número natural n y devuelve por medio de un booleano
    si es o no potencia de 2"""

    x = 2
    while n > x:
        x *= 2
    if n != x:
        return False
    return True

def solicitar_datos():
    n = int(input("Ingrese un número natural: "))
    return n

n = solicitar_datos()
print(es_potencia_de_dos(n))