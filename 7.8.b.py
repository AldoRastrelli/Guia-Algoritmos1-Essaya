def lista_al_reves(lista):
    "devuelve una nueva lista igual a la original pero invertida"
    
    
    for i in range(len(lista)-1,0,-1):
        lista.append(lista.pop(i-1))

lista = [1,2,3,4,5,6]
print("Antes:", lista)
lista_al_reves(lista)
print("Después:",lista)