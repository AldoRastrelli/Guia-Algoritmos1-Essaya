import csv 

def guardar_datos(diccionario,archivo_destino):
    """recibe un diccionario y devuelve un archivo 
    postcondiciones: el archivo se escribe en formato CSV
    como clave, valor"""

    lineas = list(diccionario.items())
    
    with open(archivo_destino,'a+') as destino:
        for linea in lineas:
            destino.write(f'{linea[0]},{linea[1]}\n')
    
diccionario = {1: 'uno',2:'dos',3:'tres',14:'catorce'}
guardar_datos(diccionario,"archivo_nuevo.txt")
            
