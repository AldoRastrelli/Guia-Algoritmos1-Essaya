from Nodo import Nodo

class ListaEnlazada:

    def __init__(self,prim = None):

        self.prim = prim
        self.len = self._len()
    
    def sumar_elementos(self):

        actual = self.prim
        return self._sumar_elementos(actual)

    def _sumar_elementos(self,actual):

        if actual.prox is None:
            return actual.dato
        
        suma = actual.dato
        actual = actual.prox
        suma += self._sumar_elementos(actual)

        return suma

    
    def _len(self):
        """calcula la longitud de la lista enlazada"""

        anterior = self.prim
        cont = 0
        while anterior is not None:
            cont += 1
            anterior = anterior.prox
        
        return cont

    def __str__(self):
        """imprime la lista enlazada con formato de lista de python"""

        lista_legible = []
        nodo = self.prim
        while nodo is not None:
            lista_legible.append(str(nodo.dato))
            nodo = nodo.prox
        return f'[{", ".join(lista_legible)}]'

    def pop(self,i=None):
        
        if i is None:
            i = self.len - 1

        elif i < 0 or i > self.len:
            raise IndexError('Índice fuera de rango')

        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox
        
        else:
            anterior = self.prim
            actual = anterior.prox

            for pos in range(1,i):
                anterior = actual
                actual = anterior.prox
            
            dato = actual.dato
            anterior.prox = actual.prox
        
        self.len -= 1
        
        return dato
    
    def remove(self,elemento):

        if self.prim is None:
            raise ValueError('La lista está vacía')
        if self.prim.dato == elemento:
            self.prim = self.prim.prox        
        else:
            anterior = self.prim
            actual = anterior.prox

            while actual is not None and actual.dato != elemento :
                anterior = actual
                actual = anterior.prox
            
            if actual == None:
                raise ValueError('El valor no está en la lista')
            anterior.prox = actual.prox
        
        self.len -= 1
    
    def insert(self,i,elemento):

        if i < 0 or i > self.len:
            raise IndexError('Posición inválida')
        
        nuevo = Nodo(elemento)

        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            anterior = self.prim
            for pos in range(1,i):
                anterior = anterior.prox
            nuevo.prox = anterior.prox
            anterior.prox = nuevo
        
        self.len += 1

    def append(self, elemento):

        self.insert(self.len,elemento)

    def index(self,elemento):

        anterior = self.prim
        cont = 0
        for pos in range(1,self.len):
            
            if anterior.dato == elemento:
                return cont
            anterior = anterior.prox
            cont += 1

        return cont

lista = ListaEnlazada()
lista.append(0)
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)
lista.append(6)
lista.append(7)


print(lista.sumar_elementos())