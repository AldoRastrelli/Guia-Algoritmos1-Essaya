def dato_es_valido(n):
    "Indica si el valor ingresado es un digito o '-1' (True). Otra cosa (False)"

    return n.isdigit() or (n == "-1")

def solicitar_datos():
    "Solicita al usuario datos que cumplan las condiciones pedidas (digit o '-1')"

    n = input("Ingrese un número natural o '-1' para salir: ")
    while not dato_es_valido(n): # not TRUE = False
        print("El dato ingresado no es válido.")
        n = input("Ingrese un número natural o '-1' para salir: ")
    return n

def contador_suma_promedio():
    """pide numeros al usuario (cortando el ciclo con -1) y calcula cuántos
    números se ingresaron, su suma y el promedio"""

    n = solicitar_datos()
    
    contador = 0
    suma = 0
    promedio = 0

    while n.isdigit():    
        contador += 1
        suma += int(n)
        promedio = suma / contador
        n = solicitar_datos()

    print("Adios.")
    return contador, suma, promedio

c, s, p = contador_suma_promedio()
print(f"Se ingresaron {c} números. Su suma es {s} y su promedio es {p}")

    