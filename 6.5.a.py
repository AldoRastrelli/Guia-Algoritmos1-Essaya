def iniciales(cadena):
    "devuelve las iniciales de una cadena"

    res = ""
    for palabra in cadena.split(" "):
        res += palabra[0]
    return res.upper()

def solicitar_cadena():
    "solicita una cadena al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

print("El siguiente programa devuelve las iniciales de una cadena ingresada.")
cadena = solicitar_cadena()
print(iniciales(cadena))

