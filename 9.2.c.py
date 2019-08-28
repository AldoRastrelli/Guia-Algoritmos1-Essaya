from random import randint as random_number

def cantidad_de_veces_valor_suma(n):
    """recibe una cantidad de iteraciones de una tirada de 2 dados a realizar
    y devuelve la cantidad de veces que se observa cada valor de la suma de los dos dados"""

    dic = {}
    sumas = []
    for _ in range(n):
        sumas.append(random_number(1,6) + random_number(1,6))
    
    cont = 0

    for i in range(len(sumas)):
        for elem in sumas:
            if sumas[i] == elem:
                cont += 1
        dic.update({sumas[i]:cont})
        cont = 0
    
    return dic

print(cantidad_de_veces_valor_suma(10))

