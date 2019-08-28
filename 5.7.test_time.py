import time
import nicoteodio
import mentira

def medir_tiempo_c():

    start = time.time()
    nicoteodio.numeros_amigos(300)
    end= time.time()
    print(end - start)

def medir_tiempo_d():    
    
    start = time.time()
    mentira.numeros_amigos(300)
    end= time.time()
    print(end - start)

medir_tiempo_c()
medir_tiempo_d()