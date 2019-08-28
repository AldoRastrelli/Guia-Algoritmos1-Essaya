import csv 

def cargar_datos(ruta):
    """recibe un archivo y devuelve un diccionario
    precondiciones: el archivo debe tener el formato clave,valor
    postcondiciones: el diccionario se devuelve con el primer
    campo como clave y el segundo como diccionario"""

    diccionario = {}

    try:
        open(ruta) as archivo:
            
            archivo_csv = csv.reader(archivo)

            for linea in archivo_csv:
                diccionario.update({ linea[0] : linea[1] })
        
        return diccionario

    except IOError as e:
        print(f'Error abriendo el archivo: {e}')

cargar_datos('animales.txt')
            
