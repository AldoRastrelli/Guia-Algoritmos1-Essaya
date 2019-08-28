def solicitar_cadena():
    "solicita una cadena al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

def orden_alfabetico(cadena1,cadena2):
    "indica qué palabra es anterior en orden alfabético"

    if len(cadena1) >= len(cadena2):
        largo = len(cadena2)
    else:
        largo = len(cadena1)

    for i in range(largo):
        if cadena1[i] == cadena2[i]:
            continue       
        if cadena1[i] > cadena2[i]:
            return cadena2
        return cadena1
        

print("El programa devuelve la cadena que tenga menor rango en orden alfabético.")

print("\nPrimera cadena:")
cadena1 = solicitar_cadena()
print("Segunda cadena:")
cadena2 = solicitar_cadena()

print(orden_alfabetico(cadena1,cadena2))