def cambiar_letras_iguales_a_la_primera_por_caracter(cadena):

    L = list(cadena)
    res = ""

    for elem in L:
        if elem == L[0]:
            res += "?"
        else:
            res += elem
        
    return res

print(cambiar_letras_iguales_a_la_primera_por_caracter("como cuanto casa ocaso acaso acarrea"))