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

def cantidad_multiplos_menores(m,n):
    "devuelve la cantidad de múltiplos de m que son menores a n"

    cont = 0
    for i in range(m,n):
        if i % m == 0 and i < n:
            cont += 1
    return cont


print("El siguiente programa devuelve la cantidad de múltiplos de un número ingresado M que son menores a otro número ingresado N.")
print("\nNúmero M:")
m = int(solicitar_datos())
print("Número N:")
n = int(solicitar_datos())

print(f"\nLa cantidad de múltiplos de {m} menores a {n} son {cantidad_multiplos_menores(m,n)}.")
