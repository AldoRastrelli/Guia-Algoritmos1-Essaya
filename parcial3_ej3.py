"""Escribir una funci ́on que reciba una pila de n ́umeros y elimine de la misma los elementos
consecutivos que est ́an repetidos. Se pueden usar estructuras auxiliares. La funci ́on no devuelve
nada, simplemente modifica los elementos de la pila que recibe por par ́ametro.

Por ejemplo: remover duplicados consecutivos(Pila([2, 8, 8, 8, 3, 3, 2, 3, 3, 3, 1, 7])) Genera: Pi-
la([2, 8, 3, 2, 3, 1, 7])."""

from pila import Pila

def eliminar_repetidos_consecutivos(pila):

    if pila.esta_vacia():
        return
    
    pila_aux = Pila()
    dato1 = pila.desapilar()
    pila_aux.apilar(dato1)

    while not pila.esta_vacia():

        dato2 = pila.desapilar()
        
        if dato1 != dato2:
            
            pila_aux.apilar(dato2)
            dato1 = dato2

    while not pila_aux.esta_vacia():

        pila.apilar(pila_aux.desapilar())


pila = Pila()
pila.apilar(2)
pila.apilar(8)
pila.apilar(8)
pila.apilar(8)
pila.apilar(3)
pila.apilar(3)
pila.apilar(2)
pila.apilar(3)
pila.apilar(3)
pila.apilar(3)
pila.apilar(1)
pila.apilar(7)
print(pila)
eliminar_repetidos_consecutivos(pila)
print(pila)


    