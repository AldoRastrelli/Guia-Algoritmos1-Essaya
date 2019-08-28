def palabra_mayor_apariciones(cadena):

    lista = cadena.split()
    apariciones = {}
    cont = 0

    for elem in lista:
        for i in range(len(lista)):
            if elem == lista[i]:
                cont +=1
        apariciones.update({elem:cont})
        cont = 0
    
    lista_apariciones = [(palabra,apariciones[palabra]) for palabra in apariciones]

    palabra_más_recurrente = (lista_apariciones[0][0],lista_apariciones[0][1])
    for conjunto in lista_apariciones:
        if conjunto[1] > palabra_más_recurrente[1]:
            palabra_más_recurrente = conjunto
    
    return palabra_más_recurrente
    

cadena = 'love of my life you have hurt me you have broken my heart and now you leave me love of my life can not you see'

print(palabra_mayor_apariciones(cadena))