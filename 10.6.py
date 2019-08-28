import string

ABC = string.ascii_lowercase

def cifrar_archivo(archivo_origen):
    """recibe un archivo de origen, lo cifra y devuelve una
    lista con las lineas cifradas
    
    precondiciones: el archivo debe existir
    postcondiciones: se devuelve una lista con las lineas 
    cifradas en sus elementos"""

    try:
        origen = open(archivo_origen)
    except:
        print('Error con el archivo de origen')
        return

    lineas_cifradas  = []
    reader = origen.readline().rstrip('\n')
    
    while reader != "":
        linea_nueva = ""
        for caracter in reader:
            if caracter in ABC:
                caracter_cifrado = ABC[(ABC.index(caracter)+13)%26]
            else:
                caracter_cifrado = caracter
            linea_nueva += caracter_cifrado
        lineas_cifradas.append(linea_nueva)
        reader = origen.readline()
    
    origen.close()
    return lineas_cifradas   
    
        
def escribir_archivo(lineas_cifradas,archivo_destino):
    """recibe una lista de lineas cifradas y las guarda en un nuevo archivo"""
    
    with open(archivo_destino,'w') as destino:
        try:
            for linea in lineas_cifradas:
                destino.write(linea)
        except TypeError:
            return

def rot(archivo_origen,archivo_destino):
    """recibe un archivo, cifra sus lineas y las guarda en el archivo de destino"""

    escribir_archivo(cifrar_archivo(archivo_origen),archivo_destino)

rot('love_of_my_life.txt','archivo_nuevo.txt')
            