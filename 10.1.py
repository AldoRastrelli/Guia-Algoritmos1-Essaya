import os

def head(archivo,n):
    """recibe un archivo y un numero N e imprime las primeras N líneas del archivo"""

    if os.path.exists(archivo):
        with open(archivo,'r') as archivo:

            for _ in range(n):
                linea = archivo.readline().rstrip('\n')
                if not linea:
                    return
                print(linea)
    else:
        print('El archivo no existe')        

head('i_want_to_break_free.txt',15)