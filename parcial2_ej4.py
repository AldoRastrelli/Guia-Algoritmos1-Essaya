#14/12/18 Recuperatorio Segundo Parcialito

def iniciales_de_palabras(cadena):

    palabras = cadena.split()
    iniciales = {}

    for palabra in palabras:
        inicial = palabra[0].lower()

        if inicial not in iniciales:
            iniciales.update({inicial:[palabra]})
            continue
        
        iniciales[inicial].append(palabra)
    
    return iniciales

print(iniciales_de_palabras('Este es el recuperatorio de Algoritmos'))
