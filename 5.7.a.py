def suma_de_divisores_de_un_numero(n):
    suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    return suma

def solicitar_datos():
    
    n = input("Ingrese un número natural: ")
    
    while not validar_datos(n):
        n = int(input("El dato ingresado no es un número natural. Ingrese un número natural: "))
    return int(n)

def validar_datos(n):
    "valida los datos ingresados por el usuario para que sea un digito"

    return n.isdigit()


n = solicitar_datos()
print(f"La suma de los divisores de {n} es {suma_de_divisores_de_un_numero(n)}")
