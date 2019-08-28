from Nodo import Nodo

class ListaEnlazada:

    def __init__(self,prim = None):

        self.prim = prim
        self.len = self._len()

    def _len(self):
        """calcula la longitud de la lista enlazada"""

        if self.prim == None:
            return 0
        
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
     
    def extender(self,lista_enlazada):
        """extiende la lista enlazada con los elementos dentro de la lista enlazada pasada por parámetro"""

        anterior = self.prim
        
        while anterior.prox is not None:
            anterior = anterior.prox
        
        nodo = lista_enlazada.prim
        anterior.prox = nodo

    def remover_todos(self,elemento):

        cont = 0
        anterior = self.prim

        if anterior:
            while anterior.dato == elemento:
                self.prim = anterior.prox
                anterior = self.prim
                actual  = anterior.prox
                cont += 1
                self.len -=1
            
            while actual is not None:
                if actual.dato == elemento:
                    anterior.prox = actual.prox
                    actual = anterior.prox
                    cont += 1
                    self.len -= 1
                else:
                    anterior = actual
                    actual = anterior.prox
        
        return cont
    
    def duplicar(self,elemento):
        """duplica el elemento ingresado por parametro, si se encuentra en la lista"""

        anterior = self.prim
        actual = anterior.prox
        while anterior.dato == elemento:
            anterior.prox = Nodo(elemento,actual)
            anterior = actual
            actual = anterior.prox
            self.len += 1
        
        while actual is not None:
            if actual.dato == elemento:
                proximo = actual.prox
                actual.prox = Nodo(elemento, proximo)
                anterior = actual
                actual = proximo
                self.len += 1
            else:
                anterior = actual
                actual = anterior.prox
    
    def filter(self,funcion):
        """recibe una funcion y devuelve una nueva lista enlazada con los elementos para los cuales
        la aplicacion de la funcion devuelve True"""

        anterior = self.prim
        actual = anterior.prox
        L2 = ListaEnlazada()
        if funcion(anterior.dato):
            L2.prim = anterior
        else:
            while not funcion(actual.dato) and actual is not None:
                anterior = actual
                actual = anterior.prox
            
            if actual is not None:
                L2.prim = actual
        
        ultimoL2 = L2.prim
        
        while actual is not None:
            if funcion(actual.dato):
                ultimoL2.prox = actual
                ultimoL2 = ultimoL2.prox
            anterior = actual
            actual = anterior.prox

        ultimoL2.prox = None

        return ListaEnlazada(L2.prim)
        