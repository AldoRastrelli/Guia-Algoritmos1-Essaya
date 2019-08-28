def maximo_de_lista_por_busqueda_lineal(lista):
    "same, but different. Versión 2"

    if not lista:
        return None

    maximo = lista[0]
    for element in lista:
        if element > maximo:
            maximo = element
    
    return maximo

print(maximo_de_lista_por_busqueda_lineal([5,4,6,9,8,10,89,14,3]))

# La manera sencilla, que piden no usar:
def maximo_de_lista(lista):
    "recibe una lista de números no ordenada y devuelve el máximo"

    lista.sort()
    return lista[-1]

def maximo_de_lista_por_funcion_max(lista):
    "same, but different"

    lista.sort()
    return max(lista)
