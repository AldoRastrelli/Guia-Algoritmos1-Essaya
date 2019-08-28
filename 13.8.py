def maximo(lista):
    """encuentra el maximo elemento de una lista por recursividad"""
    
    pivote = lista[0]
    return _maximo(pivote,lista[1:])

def _maximo(pivote,lista):

    if not lista:
        return pivote

    if pivote < lista[0]:
        pivote = lista[0]
    return _maximo(pivote,lista[1:])
    
lista = [-1,0,5,4,2]
print(maximo(lista))