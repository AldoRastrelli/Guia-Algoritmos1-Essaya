def ubicar_elemento(elemento,lista_ordenada):
    """recibe una lista ordenada y un elemento. Si el elemento se encuentra
    en la lista, encuentra su posición mediante búsqueda binaria y lo devuelve.
    Si no se encuentra, lo agrega a la lista en la posición correcta y devuelve
    dicha posición"""

    inicio = 0
    final = len(lista_ordenada) - 1

    if inicio <= elemento <= final:
        
        while inicio < final:

            medio = (inicio + final) //2
            if lista_ordenada[medio] == elemento:
                break
            if lista_ordenada[medio] < elemento:
                inicio = medio + 1
                continue
            else:
                final = medio - 1
                continue
    elif elemento > max(lista_ordenada):
        lista_ordenada.append(elemento)
    else:
        lista_ordenada.insert(0,elemento)

    return lista_ordenada.index(elemento)
            


elemento = -3
lista_ordenada = [0,1,3,4,6,7,8,9,89]

print(ubicar_elemento(elemento, lista_ordenada))