from Nodo import Nodo

class ListaCircular:

    def __init__(self,prim = None):

        self.prim = prim
        self.len = self._len()

    def _len(self):
        """calcula la longitud de la lista enlazada"""

        if self.prim == None:
            return 0
        
        actual = self.prim.prox
        cont = 1
        while actual is not self.prim:
            cont += 1
            actual = actual.prox
        return cont

    def __str__(self):
        """imprime la lista enlazada con formato de lista de python"""

        lista_legible = []
        nodo = self.prim
        if nodo is not None:
            lista_legible.append(str(nodo.dato))
            nodo = nodo.prox
        while nodo is not self.prim:
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
            
            actual = self.prim
            for i in range(1,self.len-1):
                actual = actual.prox
            actual.prox = self.prim

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
            actual = self.prim

            for i in range(1,self.len-1):
                actual = actual.prox
            actual.prox = self.prim      
        else:
            anterior = self.prim
            actual = anterior.prox

            while actual is not self.prim and actual.dato != elemento :
                anterior = actual
                actual = anterior.prox
            
            if actual == self.prim:
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
            actual = self.prim.prox

            for i in range(1,self.len):
                actual = actual.prox
            actual.prox = self.prim
                
        else:
            anterior = self.prim
            for pos in range(1,i):
                anterior = anterior.prox
            nuevo.prox = anterior.prox
            anterior.prox = nuevo
        
        self.len += 1

    def append(self, elemento):

        self.insert(self.len,elemento)

n3 = Nodo(3,None)
n2 = Nodo(2,n3)
n1 = Nodo(1,n2)
n3.prox = n1
L = ListaCircular(n1)
print(f'L: {L}')

print(f'L.len : {L.len}')

L.insert(0,'hola')
print('hola insertado')
L.insert(2,'hola')
print('hola insertado')
print(L)

L.append('final')
print('appendeado')
print(L)

L.remove('hola')
print(L)
L.remove(2)
print(L)
L.remove('final')
print(L)

L.append(4)
L.append(5)
L.append('final')
print(L)

print(L.pop(0))
print(L,L.len)
print(L.pop(3))
print(L,L.len)
print(L.pop(L.len-1))
print(L,L.len)