def es_par(n):
    """determina por medio de la recursión si un número es par"""

    # 1 es impar
    # a un número impar le antecede un par y a un par le antecede un impar

    if n == 0:
        return True
    else:
        return es_impar(n-1)

def es_impar(n):
    """determina por medio de la recursión si un número es impar"""

    if n == 0:
        return False
    else:
        return es_par(n-1)

print('4 ',es_par(4))
print('7',es_par(7))
print('5',es_par(5))
print('10',es_par(10))