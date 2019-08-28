PEDIDO_CADENA = "Ingrese una cadena de caracteres:"
PEDIDO_CARACTER = "Ingrese un caracter individual:"
PEDIDO_MAXIMO = "Ingrese un máximo de operaciones:"

def reemplazar_digitos_con_caracter(cadena,c):
    "Reemplaza los dígitos de la cadena por un caracter"

    res = ""
    lista_cadena = list(cadena)
    for char in lista_cadena:
        if char.isdigit():
            res+=c
        else:
            res+=char
    return res

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
        print(reemplazar_digitos_con_caracter(cadena,c))

        cont += 1
        continue

    print(f"\nSe ha llegado a las {m} operaciones. Adios.")

print("El siguiente programa reemplaza los números de la cadena con un caracter dado.")
maximo_operaciones()
