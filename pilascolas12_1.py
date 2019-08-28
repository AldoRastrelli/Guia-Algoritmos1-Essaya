from cola import Cola

class TorreDeControl:

    def __init__(self):

        self.arribos = Cola()
        self.partidas = Cola()
    
    def nuevo_arribo(self,avion):

        self.arribos.encolar(avion)
    
    def nueva_partida(self,avion):

        self.partidas.encolar(avion)
    
    def ver_estado(self):

        print(f'Vuelos esperando para aterrizar: {str(self.arribos)}\nVuelos esperando para despegar: {str(self.partidas)}')
    
    def asignar_pista(self):

        try:
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con éxito')
        except ValueError:
            try: 
                print(f'El vuelo {self.partidas.desencolar()} despegó con éxito')
            except ValueError:
                print('No hay vuelos en espera')
        
