def solicitar_datos():
    "Solicita datos al usuario"

    n = input("\nIngrese una cadena de caracteres: ")
    
    return n

def ultimos_tres_caracteres(n):
    "imprime los ultimos tres caracteres de de una cadena n"

    return n[(len(n)-3):]

n = solicitar_datos()
print(ultimos_tres_caracteres(n))