def solicitar_datos():
    
    n = input("Ingrese un numero. Debe ser natural: ")
    
    while not validar_datos(n):
        n = input("\nEl dato ingresado no es un número natural. Ingrese un número natural: ")
    return int(n)

def validar_datos(n):
    "valida los datos ingresados por el usuario para que sea un digito"

    return n.isdigit() #and int(n)>220)

def suma_de_divisores(n):
    suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    return suma

def numeros_amigos(m):
    "indica todos los pares de números amigos del 1 al m"

    pares = ""
    for i in range(1,m): 
        for j in range(i+1,m): # i != j e i <= j para que no se repitan parejas.
            if verifica_suma_de_div_igual_numero(i,j):
                pares += str((i,j)) + " "
            continue
    return pares

def verifica_suma_de_div_igual_numero(i,j):

    return i == suma_de_divisores(j) and j == suma_de_divisores(i)


print("\nEl programa busca todos los números perfectos desde el 1 hasta el número ingresado.")
m = solicitar_datos()
print(f"Los números amigos entre el 1 y el {m} son:\n{numeros_amigos(m)}")

#El programa tarda en ejecutar 2.7300150394439697 segundos con el número 300 (import time, start, end)
#Es apenas más sofisticado que el punto C
