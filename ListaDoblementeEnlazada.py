from NodoDobleEnlazado import Nodo

class ListaDoblementeEnlazada:

    def __init__(self,prim = None, ultimo = None):

        self.prim = prim
        self.ultimo = ultimo
        self.len = self._len()

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
            
            if i <= self.len//2 :
               actual = self._recorrer_al_derecho()
            if i > self.len//2:
                actual = self._recorrer_al_reves()

            dato = actual.dato
            
            self.len -= 1
        
        return dato
    
    def _recorrer_al_derecho(self):
        """recorre la lista hacia la derecha"""

        anterior = self.prim
        actual = anterior.prox

        for pos in range(1,i):
            anterior = actual
            actual = anterior.prox
        anterior.prox = actual.prox
        return actual
    
    def _recorrer_al_reves(self):
        """recorre la lista hacia la derecha"""

        anterior = self.ultimo
        actual = anterior.ant

        for pos in range(1,i):
            anterior = actual
            actual = anterior.ant
        anterior.ant = actual.ant
        return actual

    def remove(self,elemento):

        if self.prim is None:
            raise ValueError('La lista está vacía')
        if self.prim.dato == elemento:
            self.prim = self.prim.prox        
        else:
            if i <= self.len//2 :
               actual = self._recorrer_al_derecho()
            if i > self.len//2:
                actual = self._recorrer_al_reves()
            
            if actual is not None:
                self.len -= 1
                return
            else:
                raise ValueError('El valor no está en la lista')

    def insert(self,i,elemento):

        if i < 0 or i > self.len:
            raise IndexError('Posición inválida')
        
        nuevo = Nodo(elemento)

        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            if i <= self.len//2 :
                actual = self._recorrer_al_derecho()
                nuevo.prox = anterior.prox
                anterior.prox = nuevo
            if i > self.len//2:
                actual = self._recorrer_al_reves()
                nuevo.ant = anterior.ant
            anterior.ant = nuevo
        
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

