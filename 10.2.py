# cp.py
import os

def copiar_por_caracter(archivo):
    """lee el archivo, caracter a caracter y lo copia en otro nuevo"""

    if os.path.isfile(archivo):
        with open(archivo,'rb') as texto:
            caracter = texto.read()

            while caracter:

                with open('archivo_nuevo.txt','ab+') as copia:
                    copia.write(caracter)
                caracter = texto.read()
    else:
        print('El archivo o ruta del mismo no existe')

copiar_por_caracter('i_want_to_break_free.txt')
