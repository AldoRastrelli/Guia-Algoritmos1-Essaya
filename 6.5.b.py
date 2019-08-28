def iniciales_en_mayuscula(cadena):
    "devuelve las iniciales de una cadena en mayuscula."

    res = ""
    for palabra in cadena.split(" "):
        res += palabra.capitalize() + " "
    return res

def solicitar_cadena():
    "solicita una cadena al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

print("El siguiente programa devuelve las iniciales de una cadena ingresada, en mayuscula.")
cadena = solicitar_cadena()
print(iniciales_en_mayuscula(cadena))

