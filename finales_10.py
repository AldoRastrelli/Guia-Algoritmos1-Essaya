def armar_diccionarios(claves,valores):

    if len(claves) != len(valores):

        raise Exception("ErrorNoCoinciden")
    
    dic = {}
    
    for i in range(len(claves)):

        dic[claves[i]] = valores[i]

    return dic

claves = ['uno','dos','tres']
valores = [1, 2, 3]

print(armar_diccionarios(claves,valores))