def cantidad_de_elementos_iguales(parametro,lista):
    """la primer coincidencia del elemento en la lista y devuelve su posición"""
    
    return lista.index(parametro)

print(cantidad_de_elementos_iguales(10,[1,2,3,10,4,5,6,10,8,10,10]))