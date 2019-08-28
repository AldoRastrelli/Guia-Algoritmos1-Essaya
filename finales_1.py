VOCALES_BINARIAS = ('A','O')
VOCALES_BINARIAS_PLURAL = ('AS','OS')

def hacer_inclusivo(origen,destino):

    try:
        archivo = open(origen,'r')
    except IOError:
        print('Error al intentar abrir el archivo de entrada.')
        return
    
    try:
        archivo_modificado = open(destino,'w')
    except:
        print('Error al intentar abrir el archivo de destino')
        archivo.close()
        return
    
    linea = archivo.readline().rstrip()
    linea_modificada = ""

    while linea != "":
        
        for palabra in linea.split():

            if palabra[len(palabra)-1].upper() in VOCALES_BINARIAS:
                palabra = modificar_letras(palabra,1)
            elif palabra[len(palabra)-2:].upper() in VOCALES_BINARIAS_PLURAL:
                palabra = modificar_letras(palabra,2)
            
            linea_modificada += palabra + ' '

        linea_modificada += '\n'
        archivo_modificado.write(linea_modificada)
        linea = archivo.readline()
        linea_modificada = ""
    
    archivo.close()
    archivo_modificado.close()

def modificar_letras(palabra,cantidad):

    lista_letras = list(palabra)
    if cantidad > 1:
        final_nuevo = 'es'
    else:
        final_nuevo = 'e'
    
    lista_letras = lista_letras[:len(lista_letras)-cantidad]
    print(palabra, lista_letras)
    lista_letras.append(final_nuevo)
    print(palabra, lista_letras)

    return "".join(lista_letras)

hacer_inclusivo('hola.txt','inclusivo.txt')
