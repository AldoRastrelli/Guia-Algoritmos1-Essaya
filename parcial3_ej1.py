"""Escribir una funcion reemplazar que tome una Pila, un valor nuevo y un valor viejo y
reemplace en la Pila todas las ocurrencias de valor viejo por valor nuevo. Considerar que la
Pila tiene las primitivas apilar(dato), desapilar() y esta vacia()."""

from pila import Pila

def reemplazar(pila, valor_nuevo, valor_viejo):

    pila_aux = Pila()

    while not pila.esta_vacia():

        elemento = pila.desapilar()

        if elemento == valor_viejo:
            elemento = valor_nuevo
        
        pila_aux.apilar(elemento)
    
    while not pila_aux.esta_vacia():

        pila.apilar(pila_aux.desapilar())
    
    