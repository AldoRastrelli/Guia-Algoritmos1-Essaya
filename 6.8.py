def solicitar_cadena_binaria():
    "solicita una cadena binaria al usuario"

    cadena = input("Ingrese una cadena binaria: ")
    
    while not es_binario(cadena):
        print("La cadena ingresada no es válida.")
        cadena = input("Ingrese una cadena binaria: ")
    
    return cadena

def es_binario(cadena):
    "verifica si la cadena ingresada es un número binario"

    while not cadena.isdigit():
        return False

    for char in cadena:
        if char not in "01":
            return False
    
    return True

def convertir_binario(cadena):
    "convierte la cadena binaria en un número decimal"

    res = 0
    for i in range(len(cadena)):
        res += int(cadena[len(cadena) -1 -i]) * (2 ** i)
    return res

cadena = solicitar_cadena_binaria()
print(convertir_binario(cadena))