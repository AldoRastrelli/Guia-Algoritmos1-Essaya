def nueva_lista_al_reves(lista):
    "devuelve una nueva lista igual a la original pero invertida"
    
    L = []
    for i in range(len(lista)-1,-1,-1):
        L.append(lista[i])

    return L

lista = [1,2,3,4,5,6]
print(nueva_lista_al_reves(lista))