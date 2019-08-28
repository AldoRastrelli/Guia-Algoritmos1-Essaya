def solicitar_cadena():
    "solicita una cadena al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

def es_subcadena(cadena1,cadena2):
    "indica si la cadena2 es subcadena de cadena1"

    for i in range(len(cadena1)):
        if cadena2 == cadena1[i:i+len(cadena2)]:
            return True
        continue
    return False

print("El programa solicita dos cadenas. Luego indica si la segunda es subcadena de la primera.")

print("Primera cadena:")
cadena1 = solicitar_cadena()
print("Segunda cadena:")
cadena2 = solicitar_cadena()

print(es_subcadena(cadena1,cadena2))