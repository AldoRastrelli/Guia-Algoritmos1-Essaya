def maximo_de_lista_por_busqueda_lineal_y_posicion(lista):
    "recibe una lista de números no ordenada y devuelve el máximo y su posicion"

    if not lista:
        return None
    
    maximo = lista[0]
    
    for element in lista:
        if element > maximo:
            maximo = element


    return maximo, lista.index(maximo)

print(maximo_de_lista_por_busqueda_lineal_y_posicion([5,4,6,9,8,10,89,14,3]))