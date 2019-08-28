#ESTE EJERCICIO ES UNA MIERDA

def lista_palabras():

    elemento = input("Ingrese una elemento o enter para salir: ")

    lista = []
    while elemento != "": 
        if " " in elemento:
            continuacion = input("Ingrese una elemento o enter para salir: ")
            if continuacion != "":
                cadena = " " + elemento + continuacion
                lista.append(cadena)
                elemento = input("Ingrese una elemento o enter para salir: ")
            else:
                elemento = " " + elemento
                lista.append(elemento)
                break
        else:        
            elemento = " " + elemento
            lista.append(elemento)
            elemento = input("Ingrese una elemento o enter para salir: ")
    
    cadena = "".join(lista)
    final = cadena.split()

    return final

print(lista_palabras())

