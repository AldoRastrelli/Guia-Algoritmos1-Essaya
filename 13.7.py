from pila import Pila

def cantidad_elementos(pila):
    """calcula recursivamente cuántos elementos hay en una pila,
    suponiendo que la pila solo tiene los métodos apilar y desapilar.
    No altera el contenido de la pila"""

    contador = 0
    contador = _desapilar(pila,contador)

    return contador


def _desapilar(pila,contador):
    
    try:
        elemento = pila.desapilar()
        contador += _desapilar(pila,contador)
        pila.apilar(elemento)
        return contador+1
    except IndexError:
        return 0


pila1 = Pila()
for i in range(4):
    pila1.apilar(i)

print(cantidad_elementos(pila1))
