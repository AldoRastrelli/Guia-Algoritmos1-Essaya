"""Para una lista simplemente enlazada de números (que solo mantiene una referencia al
primer nodo) implementar la primitiva suma acumulativa() que devuelva una nueva lista (del
mismo largo) tal que el nodo i de la nueva lista contenga la suma acumulativa de los elementos
de la lista origina hasta el nodo i."""

from ListaEnlazada import LE

def suma_acumulativa(self):

    lista = LE()
    if self.prim is None:
        return lista
    
    anterior = self.prim
    lista.prim = anterior
    anterior_lista = lista.prim
    
    while anterior.prox is not None:

        actual = anterior.prox
        suma = actual.dato + anterior_lista.dato
        nodo = _Nodo(suma)

        anterior_lista.prox = nodo
        anterior_lista = nodo
        anterior = actual
