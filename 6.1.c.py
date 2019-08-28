def solicitar_datos():
    "Solicita datos al usuario"

    n = input("\nIngrese una cadena de caracteres: ")
    
    return n

def cada_dos_caracteres(n):
    "imprime los ultimos tres caracteres de de una cadena n"

    return n[::2]

n = solicitar_datos()
print(cada_dos_caracteres(n))