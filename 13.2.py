from random import choice

def rata_en_jaula(tiempo = 0):
    """ ... """

    caminos = ('1','2','3')
    camino_elegido = choice(caminos)
    print('Camino: ',camino_elegido)

    if camino_elegido == '1':
        tiempo += 3
        return rata_en_jaula(tiempo)
    elif camino_elegido == '2':
        tiempo += 5
        return rata_en_jaula(tiempo)
    elif camino_elegido == '3':
        tiempo +=7
        return tiempo
    

print('Tiempo total: ',rata_en_jaula())

