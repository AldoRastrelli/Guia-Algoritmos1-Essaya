def iniciales(cadena):
    "devuelve las palabras que empiezan con la letra A"

    res = ""
    for palabra in list(cadena.split(" ")):
        if palabra[0] in "AaÁá":
            res += palabra + " "
    return res

def solicitar_cadena():
    "solicita una cadena al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

print("El siguiente programa devuelve las palabras que empiezan con la letra A.")
cadena = solicitar_cadena()
print(iniciales(cadena))

