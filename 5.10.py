def es_primo(n):
	#Dado un número entero n, indica si es primo o no

    for i in range(2,n):
        if n % i == 0:
            return False
        continue
    return True

def solicitar_datos():
    "solicita datos al usuario que cumplan con ser digito"

    n = input("Ingrese un número entero: ")    
    
    while not dato_valido(n): # not True = False
        print("El dato ingresado no es válido.")
        n = input("Ingrese un número entero: ")          
    return int(n)

def dato_valido(x):
    "valida que el dato ingresado por el usuario sea un digito"
    
    return x.isdigit() #Devuelve TRUE or FALSE

def numeros_primos_hasta(n):
    "recibe un número natural e imprime todos los números primos que hay hasta ese número"

    primos = ""
    for i in range(1,n):
        if es_primo(i):
            primos += str(i) + "  "
        else:
            continue
    return primos

print(f"El programa imprime todos los primos hasta el numero ingresado.")
n = solicitar_datos()
print(f"\nLos números primos del 1 al {n} son:\n{numeros_primos_hasta(n)}")