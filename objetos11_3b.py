class Vector:

    def __init__(self,lista):
        """constructor de la clase. Recibe valores enteros"""

        self.items = lista

    def __validar__(self,valor):
        """valida que los datos ingresados coincidan con las características de la clase"""

        if not isinstance(valor,int):
            raise Exception('Los valores no son válidos')
        return valor
    
    def __str__(self):
        """devuelve el vector con el formato [x,y,z]"""

        return f'{self.items}'
    
    def __add__(self,otro):
        """recibe otro vector, verifica si tienen la misma cantidad de elementos y
        devuelve un nuevo vector con la suma de ambos. Si no tienen la misma dimensión,
        levanta una excepción"""

        if len(self.items) != len(otro.items):
            raise Exception('Los vectores no tienen igual dimensión')
        
        return Vector([self.items[i] + otro.items[i] for i in range(len(self.items))])