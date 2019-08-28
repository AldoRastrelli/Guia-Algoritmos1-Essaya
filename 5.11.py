def solicitar_datos():
    "solicita datos al usuario que cumplan con ser digito"

    n = input("Ingrese un número entero: ")    
    
    while not dato_valido(n): # not True = False
        print("El dato ingresado no es válido.")
        n = input("Ingrese un número entero: ")          
    return n

def dato_valido(x):
    "valida que el dato ingresado por el usuario sea un digito"
    
    return x.isdigit() #Devuelve TRUE or FALSE

def es_caracter(n,d):
    "indica si el digito d es parte de la cifra natural n"

    while n > 0.09:
        resto = n % 10
        n = n // 10
        if resto == d:
            return True
        else:
            continue
    return False

print("El programa indica si un digito D se encuentra en un número entero N.")
print("\nDígito D:")
D = float(solicitar_datos())
print("\nNúmero N:")
N = float(solicitar_datos())
print(es_caracter(N,D))