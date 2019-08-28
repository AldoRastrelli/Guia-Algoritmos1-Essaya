def reemplazar_digitos_con_caracter(cadena,c):
    "Reemplaza los dígitos de la cadena por un caracter"

    res = ""
    lista_cadena = list(cadena)
    for char in lista_cadena:
        if char.isdigit():
            res+=c
        else:
            res+=char
    return res


def solicitar_cadena_caracter():
    "solicita una cadena y un caracter al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")
    c = input("Ingrese un caracter: ")

    return cadena, c

print("El siguiente programa reemplaza los números de la cadena con un caracter dado.")
cadena,c = solicitar_cadena_caracter()
print(reemplazar_digitos_con_caracter(cadena,c))

