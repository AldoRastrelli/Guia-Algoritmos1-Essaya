def colocar_caracter_cada_tres_digitos(cadena,c):
    "Inserta un caracter cada tres digitos de la cadena"

    list_cadena = list(cadena)
    for i in range(1,len(list_cadena)//3+1):
        list_cadena.insert(i*4-1,c)
    return "".join(list_cadena)

def solicitar_cadena_caracter():
    "solicita una cadena y un caracter al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")
    c = input("Ingrese un caracter: ")

    return cadena, c

print("El siguiente programa agrega un caracter dado cada tres dígitos de la cadena.")
cadena,c = solicitar_cadena_caracter()
print(colocar_caracter_cada_tres_digitos(cadena,c))

