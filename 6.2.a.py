def separar_cadena_con_caracter(cadena,c):
    "Inserta el caracter entre cada letra de la cadena"

    return c.join(list(cadena))

def solicitar_cadena_caracter():
    "solicita una cadena y un caracter al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")
    c = input("Ingrese un caracter: ")

    return cadena, c

print("El siguiente programa separa una cadena con un caracter dado.")
cadena,c = solicitar_cadena_caracter()
print(separar_cadena_con_caracter(cadena,c))

