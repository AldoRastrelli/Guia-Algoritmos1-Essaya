from copy import deepcopy

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self,item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError('La pila está vacía')
        return self.items.pop()

    def __str__(self):

        pila_aux = deepcopy(self)
        lista = [str(pila_aux.desapilar()) for _ in range(len(self.items))]

        return f'{", ".join(lista)}'