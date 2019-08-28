PEDIDO_CADENA = "Ingrese una cadena de caracteres:"
PEDIDO_CARACTER = "Ingrese un caracter individual:"
PEDIDO_MAXIMO = "Ingrese un máximo de operaciones:"

def separar_cadena_con_caracter(cadena,c):
    "Inserta el caracter entre cada letra de la cadena"

    return c.join(list(cadena))

def solicitar_dato(mensaje):
    "solicita un dato"

    return input(f"{mensaje} ")

def maximo_operaciones():
    "limita el máximo de operaciones según el parámetro recibido"

    m = int(solicitar_dato(PEDIDO_MAXIMO))

    cont = 0
    while cont < m: 
        
        cadena = solicitar_dato(PEDIDO_CADENA)
        c = solicitar_dato(PEDIDO_CARACTER)
        print(separar_cadena_con_caracter(cadena,c))

        cont += 1
        continue

    print(f"\nSe ha llegado a las {m} operaciones. Adios.")



print("El siguiente programa separa una cadena con un caracter dado.")
maximo_operaciones()
