import re #Regular expression operations

def grep(expresion,ruta):

    try: 
        archivo = open(ruta)
    except FileNotFoundError:
        print('El archivo no existe o no se encuentra disponible')
        return 
    except:
        print('Ha ocurrido un error intentando abrir el archivo')
        return
    
    linea = next(archivo)

    while True:
        try:
            if expresion.lower() in linea.lower():
                print(linea)
            linea = next(archivo)
        
        except StopIteration:
            print('\n---- FIN DEL ARCHIVO ----\n')
            break

    archivo.close()

grep('love of my life','love_of_my_life.txt')

grep('i want to break free','i_want_to_break_free.txt')