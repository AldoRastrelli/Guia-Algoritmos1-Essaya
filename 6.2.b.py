def reemplazar_espacios_con_caracter(cadena,c):
    "Reemplaza los espacios de la cadena con un caracter"

    return c.join(cadena.split(" "))

def solicitar_cadena_caracter():
    "solicita una cadena y un caracter al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")
    c = input("Ingrese un caracter: ")

    return cadena, c

print("El siguiente programa reemplaza los espacios de la cadena con un caracter dado.")
cadena,c = solicitar_cadena_caracter()
print(reemplazar_espacios_con_caracter(cadena,c))

