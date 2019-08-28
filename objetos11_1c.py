class Intervalo:
    """representacion de un intervalo entre dos instantes de tiempo"""
    
    def __init__(self,desde,hasta):
        """constructor de la clase"""
        self.desde,self.hasta = self.__validar__(desde,hasta)
        

    def __validar__(self,desde,hasta):
        """valida que los datos ingresados coincidan con las características de la clase"""

        if not isinstance(desde,(int)) or not isinstance(hasta,(int)) or not 0 < desde < hasta:
            raise Exception('Los valores no son válidos')

        return desde,hasta

    def duracion(self):
        """devuelve la duracion en segundos del intervalo"""
        return self.hasta - self.desde

    def interseccion(self,otro):
        """devuelve un nuevo intervalo resultante de la intersección entre ambos,
        o lanza una excepcion si es nula"""
    
        cota_izquierda,cota_derecha = max(self.desde,otro.desde),min(self.hasta,otro.hasta)
        if cota_izquierda < cota_derecha:
            return cota_izquierda,cota_derecha
        else:
            raise Exception('El intervalo de intersección no existe.')

