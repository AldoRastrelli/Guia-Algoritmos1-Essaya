class Prenda:

    def __init__(self,tipo,espacio_a_ocupar):
        """constructor de la clase.
        precondiciones: tipo debe ser string y espacio_a_ocupar debe ser int>0"""

        
        try:
            assert self.__validar_tipo__(tipo,espacio_a_ocupar) == True
        except:
            print('Los datos ingresados no son válidos')
        else:
            self.tipo = tipo
            self.espacio_a_ocupar = espacio_a_ocupar            

    def __validar_tipo__(self,tipo,espacio_a_ocupar):
        """verifica type(tipo)=str y type(espacio_a_ocupar)=int"""
        return (isinstance(tipo,str) and isinstance(espacio_a_ocupar,int) and espacio_a_ocupar>0)

    def __repr__(self):

        return f"Prenda({str(self.tipo)},{self.espacio_a_ocupar})"

class Perchero:

    def __init__(self,espacio_libre):
        """constructor de la clase.
        precondiciones: espacio_libre debe ser int
        postcondiciones: el atributo es un int"""

        try:
            assert self.__validar_tipo__(espacio_libre) == True
        except:
            print('Los datos ingresados no son válidos')
        else:
            self.espacio_libre = espacio_libre
            self.prendas_colgadas = {}

    def __validar_tipo__(self,espacio_libre):

        return isinstance(espacio_libre,int) and espacio_libre>0

    def colgar(self,ropa):
        
        try:
            assert ropa.espacio_a_ocupar <= self.espacio_libre
        except AssertionError:
            print('Exception: No hay espacio para colgar la prenda')
        else:       
            self.prendas_colgadas.update({ropa.tipo:ropa.espacio_a_ocupar})
            self.espacio_libre -= ropa.espacio_a_ocupar

    def sacar(self,item):

        try:
            assert item in self.prendas_colgadas
        except Exception:
            print(f'Exception: No se encontró la prenda')
        else:
            ropa = Prenda(item,self.prendas_colgadas[item])
            self.espacio_libre += self.prendas_colgadas[item]
            self.prendas_colgadas.pop(item)
            return ropa

    def espacio_disponible(self):

        print(self.espacio_libre)