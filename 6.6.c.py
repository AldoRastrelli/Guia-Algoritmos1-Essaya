def solicitar_cadena():
    "solicita una cadena al usuario"

    cadena = input("Ingrese una cadena de caracteres: ")

    return cadena

def devolver_sentido_inverso(n):
    "imprime los ultimos tres caracteres de de una cadena n"

    return n[::-1]

def es_palindromo(cadena,anedac):
    "me indica si la cadena se lee igual al derecho y al revés"

    return cadena == anedac

print("El programa indica si la cadena ingresada es un palíndromo (se lee igual del derecho y del revés).")

cadena = "".join(solicitar_cadena().split(" "))
anedac = devolver_sentido_inverso(cadena)
print(es_palindromo(cadena,anedac))