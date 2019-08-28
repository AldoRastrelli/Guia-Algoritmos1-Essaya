LONG = len(list_cadena)

def dar_formato_miles(cadena):
    "Inserta un caracter cada tres digitos de la cadena"

    list_cadena = list(cadena)
    for i in range(-1,-LONG//3-1,-1):
        if -4*i <= LONG:
            list_cadena.insert(4*i+1,".")
    return "".join(list_cadena)

def solicitar_cadena():
    "solicita una cadena de números"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

print("El siguiente programa da formato con separación de miles a un número.")
cadena = solicitar_cadena()
print(dar_formato_miles(cadena))