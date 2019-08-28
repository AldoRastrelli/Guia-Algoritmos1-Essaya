# vector :: tupla (para trabajar con elemento inmutables).

def producto_vectorial(tupla1,tupla2):
    """recibe dos tuplas y devuelve el producto vectorial entre sí"""

    if verificar_dimension(tupla1,tupla2) == True:
        res = 0
        for i in range(len(tupla1)):
            res += tupla1[i] * tupla2[i]
        return res
    return ("Los vectores no tiene la misma dimensión.")


def verificar_dimension(tupla1,tupla2):
    "verifica que ambas tuplas tengan la misma dimensión"

    return len(tupla1) == len(tupla2)

tupla1 = ( 1 , -2 )
tupla2 = ( 3 , 4 , 10)
print(producto_vectorial(tupla1,tupla2))