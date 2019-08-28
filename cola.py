from copy import deepcopy

class Cola:

    def __init__(self):
        self.items = []
    
    def encolar(self,item):
        self.items.append(item)
    
    def desencolar(self):

        if self.esta_vacia():
            raise ValueError('La cola está vacía')
        return self.items.pop(0)
    
    def esta_vacia(self):

        return len(self.items) == 0

    def __str__(self):

        cola_aux = deepcopy(self)
        lista = [str(cola_aux.desencolar()) for i in range(len(cola_aux.items))]

        return f'{", ".join(lista)}'

    
