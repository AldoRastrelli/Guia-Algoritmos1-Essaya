def empaquetar(lista):
    "Indica la repetición de valores consecutivos mediante una tupla y devuelve la lista de tuplas"
    
    lista_nueva = []
    cont = 1
    for i in range(1,len(lista)):

        
        if lista[i] == lista[i-1]:
            cont += 1
        else:
            tupla = (lista[i-1],cont)
            lista_nueva.append(tupla)
            cont = 1 
        
        if i == len(lista)-1:
            tupla = (lista[i-1],cont)
            lista_nueva.append(tupla)      

    return lista_nueva

lista = [1,1,1,3,5,1,1,3,3]
print(empaquetar(lista))
