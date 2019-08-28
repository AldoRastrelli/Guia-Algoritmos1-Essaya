"""Escribir un m etodo que invierta una ListaEnlazada utilizando una Pila como estructura
auxiliar y considerando que lista solo tiene una referencia al primer nodo."""

from pila import Pila
from nodo import _Nodo

def invertir(self):

    pila = Pila()

    if self.prim is None:
        return
    
    nodo = self.pop() #utilizo self.pop porque el enunciado no indica que se necesite recorrer la lista una sola vez.

    while nodo is not None:

        pila.apilar(nodo)
        nodo = self.pop()
    
    proximo = None

    while not pila.esta_vacia():

        nodo_nuevo = _Nodo()
        nodo_nuevo.dato = pila.desapilar()
        nodo_nuevo.prox = proximo
        proximo = nodo_nuevo
    
    self.prim = proximo
