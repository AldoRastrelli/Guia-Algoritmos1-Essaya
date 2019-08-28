

*** FALTA TERMINAR: EL APPEND (O EL INSERT AL FINAL) NO FUNCIONA. ARMAR LA LISTA, LEN
ULTIMO ELEMENTO E INSERT EN OTROS LUGARES SI ANDA ***


from NodoDobleEnlazado import Nodo

class ListaDoblementeEnlazada:

    def __init__(self,prim = None, ultimo = None):

        self.prim = prim
        self.len = self._len()
        self.ultimo = self._ultimo_elemento()
        

    def _ultimo_elemento(self):

        ultimo = self.prim
        
        if ultimo is not None:
            for _ in range(0,self.len):
                ultimo = ultimo.prox
        return ultimo

    def _len(self):
        """calcula la longitud de la lista enlazada"""

        actual = self.prim
        cont = 0

        while actual is not None:
            cont += 1
            actual = actual.prox
        print(cont)
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
               actual,anterior = self._recorrer_al_derecho(i)
               anterior.prox = actual.prox
            if i > self.len//2:
                actual,anterior = self._recorrer_al_reves(i)
                anterior.ant = actual.ant
            dato = actual.dato
            self.len -= 1
        self.ultimo = self._ultimo_elemento()

        return dato
    
    def _recorrer_al_derecho(self,iterador):
        """recorre la lista hacia la derecha"""

        anterior = self.prim
        actual = anterior.prox

        for pos in range(1,iterador):
            anterior = actual
            actual = anterior.prox
        return actual,anterior
    
    def _recorrer_al_reves(self,iterador):
        """recorre la lista hacia la derecha"""

        anterior = self.ultimo
        actual = anterior.ant

        for pos in range(0,self.len-iterador):
            anterior = actual
            actual = anterior.ant
        return actual,anterior

    def remove(self,elemento):

        if self.prim is None:
            raise ValueError('La lista está vacía')
        if self.prim.dato == elemento:
            self.prim = self.prim.prox        
        else:
            if i <= self.len//2 :
               actual,anterior = self._recorrer_al_derecho(i)
            if i > self.len//2:
                actual,anterior = self._recorrer_al_reves(i)
            
            if actual is not None:
                self.len -= 1
                return
            else:
                raise ValueError('El valor no está en la lista')
        self.ultimo = self._ultimo_elemento()

    def insert(self,i,elemento):

        if i < 0 or i > self.len:
            raise IndexError('Posición inválida')
        
        nuevo = Nodo(elemento)

        if i == 0:
            nuevo.prox = self.prim
            self.prim = nuevo
            nuevo.ant = None
        else:
            if i <= self.len//2 :
                actual,anterior = self._recorrer_al_derecho(i)
                nuevo.prox = anterior.prox
                anterior.prox = nuevo
                nuevo.ant = anterior
            if i > self.len//2:
                print(F'nuevo: {nuevo}')
                actual,anterior = self._recorrer_al_reves(self.len-i)
                print(f'actual: {actual}, anterior: {anterior}')
                nuevo.ant = anterior
                nuevo.prox = actual
                anterior.prox = nuevo
                if actual is not None:
                    actual.ant = nuevo

        self.ultimo = self._ultimo_elemento()
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


n3 = Nodo(3,None,None)
n2 = Nodo(2,n3,None)
n1 = Nodo(1,n2,None)
n3.ant = n2
n2.ant = n1

L = ListaDoblementeEnlazada(n1)
print(f'L: {L}')

print(f'L.len : {L.len}')
L.insert(0,'hola')
print('hola insertado')
L.insert(3,'hola')
print('hola insertado')
print(L)
print(f'self.ultimo: {str(L.ultimo)}')
L.append('final')
print('appendeado')
print(f'self.ultimo: {str(L.ultimo)}')
print(L)

"""
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
print(L,L.len)"""