def lista_de_numeros_que_terminan_en_cero(lista):
    "recibe una lista con números enteros y devuelve una nueva lista con los elementos de la lista original que terminan en cero"

    terminan_en_cero = []
    for elem in lista:
        if elem % 10 == 0 :
            terminan_en_cero.append(elem)
    
    return terminan_en_cero

print(lista_de_numeros_que_terminan_en_cero([4,23,40,-7,0,14,1000,-760]))
