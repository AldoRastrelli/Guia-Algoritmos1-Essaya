from string import ascii_letters
from string import ascii_uppercase
from string import ascii_lowercase

VOCALES = "AEIOUaeiouáéíóúÁÉÍÓÚ"
TILDES = "áéíóúÁÉÍÓÚ"
ABC = list(ascii_letters) + list(ascii_uppercase) + list(ascii_lowercase) + list("ñ")

def iniciales(cadena,consonantes):
    "devuelve las palabras que empiezan con la letra A"

    res = ""
    for char in cadena:
        if char not in consonantes:
            res += char
    return res

def solicitar_cadena():
    "solicita una cadena al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

for char in ABC:
    if char in VOCALES:
        ABC.remove(char)
consonantes=ABC

print("El siguiente programa devuelve las letras vocales.")
cadena = solicitar_cadena()
print(iniciales(cadena,consonantes))
