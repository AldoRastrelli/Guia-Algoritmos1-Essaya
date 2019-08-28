def solicitar_datos():
    "Solicita datos al usuario"

    n = input("\nIngrese una cadena de caracteres: ")
    
    return n

def devolver_cadena_reflejada(n):
    "imprime los ultimos tres caracteres de de una cadena n"

    return n[::] + n[::-1]

n = solicitar_datos()
print(devolver_cadena_reflejada(n))