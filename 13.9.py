def replicar_elementos(lista,n):
    """por medio de la recursión, se replican los elementos de una lista una n cantidad de veces"""

    m = n * len(lista) 
    return _replicar(lista,m,n)

def _replicar(lista,m,n):

    if no_replicar(lista,m):
        return []

    elem = lista.pop()
    lista = _replicar(lista,m-n,n)
    lista += [elem] * n
    return lista

def no_replicar(lista,n):
    
    return n <= 0 or not lista

print(replicar_elementos([1,2,3,7],1))
