DENOMINACIONES = [1,2,5,10,20,50,100,500,1000]

class Caja:

    def __init__(self, diccionario):

        self.dinero = {}

        self.agregar(diccionario)

    def __str__(self):
        
        total = 0
        for clave in self.dinero:
            total += clave * self.dinero[clave]

        return f'Caja {self.dinero}. Total = {total} pesos'
    
    def __validar_denominacion__(self,diccionario):

        for clave in diccionario:
            if clave not in DENOMINACIONES:
                raise ValueError(f'Denominacion {clave} no permitida.')
        return True

    def agregar(self,diccionario):

        if self.__validar_denominacion__(diccionario):
            
            for clave in diccionario:
                if clave not in self.dinero:
                    self.dinero[clave] = 0
            
                self.dinero[clave] += diccionario[clave]
            
    def quitar(self,diccionario):

        if self.__validar_denominacion__(diccionario):
            
            for clave in diccionario:
                if clave not in self.dinero or diccionario[clave] > self.dinero[clave]:
                    raise ValueError(f'No hay suficientes billetes de denominación {clave}')
                self.dinero[clave] -= diccionario[clave]

                if self.dinero[clave] == 0:
                    self.dinero.pop(clave)

            