def solicitar_dos_numeros():
    "solicita dos números al usuario"

    while True:
        m = input("\nIngrese su primer número: ")
        if m.isdigit() == False:
            print("El número no es válido. Intente nuevamente.")
            continue
        break
    while True:
        n = input("Ingrese su segundo número: ")
        if n.isdigit() == False:
            print("El número no es válido. Intente nuevamente.")
            continue
        break
    if m>n:
        return float(m),float(n)
    return float(n),float(m)

def maximo_comun_divisor(m,n):
    "calcula el máximo común divisor de ambos números"

    
    while m % n != 0:
        r = m % n
        m = n
        n = r
    return n
    

print("\nEl programa calcula el máximo común divisor entre dos números enteros.")
m,n = solicitar_dos_numeros()
mcd = maximo_comun_divisor(m,n)

print(f"El máximo común divisor entre {m} y {n} es {mcd}")