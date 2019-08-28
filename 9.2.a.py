def cantidad_de_apariciones_palabras(cadena):
    """recibe una cadena y devuelve un diccionario
    con la cantidad de apariciones de cada palabra en la cadena"""

    lista = cadena.split()
    dic = {}
    cont= 0

    for i in range(len(lista)):
        for elem in lista:
            if lista[i] == elem:
                cont += 1
        dic.update({lista[i]:cont})
        cont = 0
    
    return dic

cadena = 'we are the champions my friend and we will keep on trying till the end we are the champions we are the champions no time for losers cause we are the champions of the world'
print(cantidad_de_apariciones_palabras(cadena))