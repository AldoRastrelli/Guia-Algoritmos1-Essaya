def solicitar_datos():
    
    minimo = int(input("Ingrese un número natural, este será el mínimo: "))
    maximo = int(input("Ingrese un número natural, mayor que el anterior: "))

    while not validar_datos(maximo,minimo):
        print("\nLos números ingresados no cumplen con lo pedido: ")
        minimo = int(input("Ingrese un número natural, este será el mínimo: "))
        maximo = int(input("Ingrese un número natural, mayor que el anterior: "))

    return minimo,maximo

def validar_datos(maximo,minimo):
    "valida los datos ingresados por el usuario para que sea un digito"
    if maximo>minimo:
        return True
    return False

def es_potencia_de_dos(n):
    """recibe un número natural n y devuelve por medio de un booleano
    si es o no potencia de 2"""

    x = 2
    while n > x:
        x *= 2
    if n != x:
        return False
    return True

def suma_de_potencias_de_dos_entre_dos_parametros(minimo,maximo):
    """Suma entre sí todas las potencias de 2 que se encuentren entre el rango
    definido por minimo y maximo"""

    suma = 0
    for i in range(minimo,maximo):
        if es_potencia_de_dos(i):
            suma += i
    return suma

minimo, maximo = solicitar_datos()
suma = suma_de_potencias_de_dos_entre_dos_parametros(minimo,maximo)
print(f"La suma de todas las potencias de 2 entre {minimo} y {maximo} es {suma}")

