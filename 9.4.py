def palabra_mas_larga_por_caracter(cadena):
    """recibe un texto y para cada caracter presente en el texto devuelve
    la cadena más larga en la que se encuentra ese caracter"""

    dicc = {}

    """for palabra in cadena.split():
        for caracter in palabra:
            if caracter not in dicc or len(palabra) > len(dicc[caracter]):
                dicc.update({caracter:palabra})"""

    [dicc.update({caracter:palabra}) for palabra in cadena.split() for caracter in palabra if caracter not in dicc or len(palabra) > len(dicc[caracter])]
    
    return dicc

print(palabra_mas_larga_por_caracter('ana aldana banana americana alejandria'))