def maximo_de_cadena_por_busqueda_lineal_y_posicion(cadena):
    "recibe una cadena de números no ordenada y devuelve el máximo y su posicion"

    maximo = cadena[0]
    
    for element in cadena:
        if element > maximo:
            maximo = element

    print(sorted(cadena))
    return maximo, cadena.index(maximo)

print(maximo_de_cadena_por_busqueda_lineal_y_posicion('091845761234j56789'))

"""Los caracteres de una cadena siguen el orden determinado por la tabla ASCII.
Por lo tanto, los números se arreglan de menor a mayor, las letras en orden
alfabético, y los números van antes que las letras"""

"""Las cadenas no pueden pasar por un proceso de sort para dejarlas en orden pero sí por un 
sorted, creando una nueva lista"""