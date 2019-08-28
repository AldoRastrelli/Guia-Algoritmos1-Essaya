"""un año bisiesto es divisible por 4, no es divisible por 100 pero sí
 es divisible por 400"""

def indicar_año_bisiesto(año):
    "indica si el año dado por el usuario es bisiesto"

    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    return False

print(indicar_año_bisiesto(int(input("Indique el año: "))))

assert indicar_año_bisiesto(2000) == True
assert indicar_año_bisiesto(2020) == True
assert indicar_año_bisiesto(2001) == False

