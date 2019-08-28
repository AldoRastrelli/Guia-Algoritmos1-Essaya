import csv
import os

def pasajes_avion(ruta):

    try:
        archivo = open(ruta,'r')
    
    except FileNotFoundError:
        return 'El archivo no se encuentra'

    archivo_csv = csv.reader(archivo,delimiter=',') #lee las lineas en forma de lista, devuelve conjunto de listas
    pasajes = {}
    vuelos = []
    id_vuelo = next(archivo_csv)

    while True:
        try:
            vuelos.append(id_vuelo) #lista de listas
            id_vuelo = next(archivo_csv)
        except StopIteration:
            break

    archivo.close()

    for id_vuelo in vuelos:

        fecha = id_vuelo[0]
        destino = id_vuelo[1]
        precio = id_vuelo[2]

        for i in range(len(vuelos)):
        
            if destino not in pasajes:
                pasajes.update({destino:(fecha,precio)})
                continue
            
            if destino == vuelos[i][1] and float(vuelos[i][2]) < float(pasajes[destino][1]):
                pasajes.update({destino:(vuelos[i][0],vuelos[i][2])})
            
    for destino in pasajes:
        pasajes.update({destino:(pasajes[destino][0],f'{int(pasajes[destino][1]):,}')})

    return pasajes

print(pasajes_avion("pasajes_avion.txt"))
                
            
            
            





    