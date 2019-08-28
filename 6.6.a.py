VOCALES = "AEIOUaeiouáéíóúÁÉÍÓÚ"

def iniciales(cadena):
    "devuelve las palabras que empiezan con la letra A"

    res = ""
    for char in cadena:
        if char not in VOCALES:
            res += char
    return res

def solicitar_cadena():
    "solicita una cadena al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

print("El siguiente programa devuelve las palabras que empiezan con la letra A.")
cadena = solicitar_cadena()
print(iniciales(cadena))

