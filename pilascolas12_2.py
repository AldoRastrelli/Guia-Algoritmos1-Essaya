from cola import Cola
from pila import Pila

class Impresora:

    def __init__(self, nombre, capacidad_tinta):

        self.nombre = nombre
        self.capacidad_max = capacidad_tinta
        self.capacidad = self.capacidad_max
        self.cola_de_impresion = Cola()

    def encolar(self,archivo):

        self.cola_de_impresion.encolar(archivo)
    
    def imprimir(self):

        if not self.capacidad:
            print('No tengo tinta :(')
            return   
        print(f'{self.cola_de_impresion.desencolar()} impreso.')
        self.capacidad -= 1

    def cargar_tinta(self):

        self.capacidad = self.capacidad_max

class Oficina:

    def __init__(self):

        self.impresoras = []
    
    def agregar_impresora(self,impresora):

        self.impresoras.append(impresora)

    def obtener_impresora_libre(self):

        minimo = self.contar_archivos(self.impresoras[0])
        impresora_min = self.impresoras[0]

        for equipo in self.impresoras[1:]:

            archivos = self.contar_archivos(equipo)

            if archivos < minimo:
                impresora_min = equipo
                minimo = archivos
        
        return impresora_min

    def contar_archivos(self, equipo):

        if equipo.cola_de_impresion.esta_vacia():
            return 0

        i = 1
        cola_aux = Cola()
        while not equipo.cola_de_impresion.esta_vacia():
            cola_aux.encolar(equipo.cola_de_impresion.desencolar())
            i +=1
        
        while not cola_aux.esta_vacia():
            equipo.cola_de_impresion.encolar(cola_aux.desencolar())

        return i

    def impresora(self,nombre):

        for equipo in self.impresoras:

            if equipo.nombre == nombre:
                return equipo

        




