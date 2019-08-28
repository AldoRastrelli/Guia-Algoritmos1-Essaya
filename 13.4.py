def posicion_de(cadena1, cadena2, pos = 0, posiciones = []):
    """recibe como parametros dos cadenas (cadena1 y cadena 2) y
    devuelve una lista con las posiciones en donde se encuentra b dentro de a"""

    if cadena1 == cadena2:
        posiciones.append(pos)
        return posiciones

    if cadena1[pos] != cadena2[0]:
        pos += 1
    else:
        if cadena1[pos:pos+len(cadena2)] == cadena2:
            posiciones += [pos]
            pos += len(cadena2)

    if pos < len(cadena1):
        return posicion_de(cadena1,cadena2,pos,posiciones)
    return posiciones

print(posicion_de('un tete a tete con Tete', 'te'))
