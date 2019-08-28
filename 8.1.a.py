def cantidad_de_elementos_iguales(parametro,lista):
    """busca todos los elementos que coinciden con el pasado por parámetro
        y devuelve la cantidad de coincidencias encontradas"""
    
    cont = 0
    for elem in lista:
        if elem == parametro:
            cont += 1
    
    return cont

print(cantidad_de_elementos_iguales(10,[1,2,3,10,4,5,6,10,8,10,10]))