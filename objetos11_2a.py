class Fraccion:

    def __init__(self,x,y):
        """constructor de la clase"""
        self.x,self.y = self.__validar__(x,y)


    def __validar__(self,x,y):
        """valida que los datos ingresados coincidan con las características de la clase"""

        if not isinstance(x,(int)) or not isinstance(y,(int)):
            raise Exception('Los valores no son válidos')
        return x,y

    def __str__(self):
        """devuelve los atributos de self en forma de cadena"""

        return (f'{self.x}/{self.y}')

