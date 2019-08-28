def solicitar_datos():
    
    n = input("Ingrese un numero máximo. Debe ser natural: ")
    
    while not validar_datos(n):
        n = int(input("\nEl dato ingresado no es un número natural. Ingrese un número natural: "))
    return int(n)

def validar_datos(n):
    "valida los datos ingresados por el usuario para que sea un digito"

    return n.isdigit()

def suma_de_divisores_de_un_numero(n):
    suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    return suma

def numeros_perfectos(m):
    "indica todos los números perfectos del 1 al m"

    suma = ""
    for i in range(1,m):
        if i == suma_de_divisores_de_un_numero(i):
            suma += str(i) + " "
    return suma

print("\nEl programa busca todos los números perfectos desde el 1 hasta el número ingresado.")
m = solicitar_datos()
print(f"Los números perfectos del 1 al {m} son:\n{numeros_perfectos(m)}")

