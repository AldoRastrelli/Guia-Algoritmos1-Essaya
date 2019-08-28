import csv

def cut(ruta, delimitador, campos_a_imprimir):
    """recibe un archivo de texto, un delimitador y
    campos a imprimir, e imprime únicamente esos campos separados por ese delimitador"""

    with open(ruta) as archivo:

        reader = csv.DictReader(archivo,delimiter = delimitador) #crea un diccionario ordenado, saltea encabezado
        
        for valores in reader:
            valores_a_imprimir = [valores[campo] for campo in campos_a_imprimir]
            print(delimitador.join(valores_a_imprimir))

def cut_v2(ruta,delimitador,campos_a_imprimir):

    with open(ruta) as archivo:

        reader = csv.reader(archivo, delimiter = delimitador)
        campos = next(reader)
        indices = [campos.index(item) for item in campos_a_imprimir]
        
        valores_a_imprimir = [[valores[i] for i in indices] for valores in reader]
        
        print(delimitador.join(campos_a_imprimir).upper())
        for elementos in valores_a_imprimir:
            print(delimitador.join(elementos))

cut_v2('cohabitantes.txt',',',('nombre','años','especie'))



