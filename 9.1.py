def tuplas_a_diccionario(lista):
    """recibe una lista de tuplas y devuelve un diccionario en donde las claves son los primeros
    elementos de las tuplas y los valores una lista con los segundos"""

    dic = {}
    lista_valores = []

    for tupla in lista:
        dic.update({tupla[0]:[]})
    for tupla in lista:
        dic[tupla[0]].append(tupla[1])
    
    return dic

lista_traducciones_varias= [
    ('hola','hello'),
    ('perro','dog'),
    ('hola','bonjour'),
    ('negro','noir'),
    ('amor','love'),
    ('rojo','red'),
    ('amor','amour'),
    ('gato','chat'),
    ('vestido','robes'),
    ('gato','cat'),
    ('negro','black'),
    ('rojo','rouge'),
    ('vestido','dress')
]

print(tuplas_a_diccionario(lista_traducciones_varias))