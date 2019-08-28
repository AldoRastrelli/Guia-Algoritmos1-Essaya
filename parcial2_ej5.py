class Azucarera:

    def __init__(self,gramos):

            self.maximo = self._validar_int(gramos)
            self.contenido = 0
        
    def _validar_int(self,gramos):

        if (isinstance(gramos,int) and gramos > 0):
            return gramos
        else:
            print('el ingresado no es válido')
    
    def poner_azucar(self,azucar):

        espacio = self.maximo - self.contenido
        azucar = abs(azucar)
        
        if azucar >= espacio:
            raise ValueError('No hay lugar para tanta azúcar.')
        else:
            self.contenido += azucar
    
    def sacar_azucar(self,azucar):

        if azucar >= self.contenido:
            raise ValueError('No hay tanta azúcar!')
        else:
            self.contenido -= azucar
        
    def azucar(self):

        azucar = Azucar(self.contenido)
        return f'{Azucar.__repr__(azucar)}'

    def __repr__(self):

        return f'Azucarera con {self.contenido}/{self.maximo} gr'

class Azucar:

    def __init__(self,cantidad=0):

        self.azucar = cantidad

    def __repr__(self):

        return f'{self.azucar} gr.'
