def solicitar_datos():
    "Solicita datos al usuario"

    n = input("\nIngrese una cadena de caracteres: ")
    
    return n

def primeros_dos_caracteres(n):
    "imprime los primeros dos caracteres de de una cadena n"

    return n[:2]

n = solicitar_datos()
print(primeros_dos_caracteres(n))