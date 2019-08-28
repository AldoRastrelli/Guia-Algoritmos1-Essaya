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
        