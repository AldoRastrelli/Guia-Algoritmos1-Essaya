PEDIDO_CADENA = "Ingrese una cadena de caracteres:"
PEDIDO_CARACTER = "Ingrese un caracter individual:"
PEDIDO_MAXIMO = "Ingrese un máximo de operaciones:"

def colocar_caracter_cada_tres_digitos(cadena,c):
    "Inserta un caracter cada tres digitos de la cadena"

    list_cadena = list(cadena)
    for i in range(1,len(list_cadena)//3+1):
        list_cadena.insert(i*4-1,c)
    return "".join(list_cadena)

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
        print(colocar_caracter_cada_tres_digitos(cadena,c))

        cont += 1
        continue

    print(f"\nSe ha llegado a las {m} operaciones. Adios.")

print("El siguiente programa agrega un caracter dado cada tres dígitos de la cadena.")
maximo_operaciones()
