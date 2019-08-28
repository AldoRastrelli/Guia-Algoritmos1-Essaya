#wc.py

def wc(ruta):
    """recibe un archivo e imprime por pantalla cuántas lineas, palabras y caracteres conetiene

    precondiciones: el archivo no debe estar vacío"""

    try:
        with open(ruta) as archivo:
            lineas = []
            linea = archivo.readline() #le saco el encabezado leyéndolo una vez

            while linea != "":
                lineas.append(linea)
                linea = archivo.readline()

            return (
                contar_lineas(lineas),
                contar_palabras(lineas),
                contar_caracteres(lineas)
            )
    except FileNotFoundError:
        print('El archivo no existe o no se encuentra disponible')
        return 
    except:
        print('Ha ocurrido un error intentando abrir el archivo')
        return 

def contar_lineas(lista_de_lineas):
    """cuenta la cantidad de líneas que tiene una lista de lineas de un archivo"""

    return len(lista_de_lineas)

def contar_palabras(lista_de_lineas):
    """cuenta al cantidad de palabras que tiene una lista de lineas de un archivo"""

    cantidad_de_palabras = [len(linea.split()) for linea in lista_de_lineas]
    return sum(cantidad_de_palabras)

def contar_caracteres(lista_de_lineas):
    """cuenta la cantidad de caracteres que tiene una lista de lineas de un archivo"""

    cont = 0
    for linea in lista_de_lineas:
        for caracter in linea:
            cont +=1
    return cont

lineas,palabras,caracteres = wc('love_of_my_life.txt')

print(f'Cantidad de lineas: {lineas}\nCantidad de palabras: {palabras}\nCantidad de caracteres: {caracteres}')
