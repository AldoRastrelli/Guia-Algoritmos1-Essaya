def listas_mayores_menores_iguales(lista,k):
    "devuelve tres listas, una con los elementos de lista menores a k, otra con los mayores y otra con los iguales"

    menores = []
    mayores = []
    iguales = []

    for elemento in lista:
        if elemento < k:
            menores.append(elemento)
        elif elemento > k:
            mayores.append(elemento)
        else:
            iguales.append(elemento)
            
    return menores, mayores, iguales
      
menores,mayores,iguales = listas_mayores_menores_iguales([1,2,3,4,5,6,7,8,9,10,11,12,13],11)
print(f'Los menores son {menores}, los mayores son {mayores}, los iguales son {iguales}.')