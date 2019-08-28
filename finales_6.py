LLAVE_CORRECTA = 5

def comparar_llaves(a,b):

    if a > b:
        return 1
    if a < b:
        return -1
    return 0
    
def probar_llave(x):

    if x > LLAVE_CORRECTA:
        return 1
    if x < LLAVE_CORRECTA:
        return -1
    return 0

def buscar_llave(bolsa_llaves):

    print(f"bolsa llaves: {bolsa_llaves}")
    llave_pivote = bolsa_llaves[len(bolsa_llaves)//2]
    print(f'Llave pivote: {llave_pivote}')
    tamaño = probar_llave(llave_pivote)
    print("tamaño: ",tamaño)
    if tamaño == 0:
        return llave_pivote
    
    bolsa_chica = []

    if tamaño == 1:
        for llave in bolsa_llaves:
            if comparar_llaves(llave,llave_pivote) <0:
                bolsa_chica.append(llave)
    
    else:
        for llave in bolsa_llaves:
            if comparar_llaves(llave,llave_pivote) > 0:
                bolsa_chica.append(llave)
    
    return buscar_llave(bolsa_chica)

bolsa_llaves = [1,6,4,90,45,7,3,6,5,150]

print(buscar_llave(bolsa_llaves))