def listas_mayores_menores_iguales(lista,k):
    "devuelve los elemento de lista multiplos de k"

    multiplos = []

    for elemento in lista:
        if elemento % 2 == 0:
            multiplos.append(elemento)
        
    return multiplos
      
k = 2
multiplos = listas_mayores_menores_iguales([2,4,6,8,10,15,13,7,5,9],k)
print(f'{multiplos} son múltiplos de {k}')