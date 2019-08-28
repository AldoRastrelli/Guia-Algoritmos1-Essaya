"""3) Escribir una funci on que reciba una palabra y devuelva una lista con todas las rotaciones
de esa palabra. Por ejemplo, si recibe: ’rotar’, debe devolver:
[’rotar’,’otarr’,’tarro’,’arrot’,’rrota’]"""

def  rotar(palabra):
    "recibe una palabra y devuelve una lista con todas las rotaciones de esa palabra"

    lista = list(palabra)
    rotaciones = []

    rotaciones.append(palabra)

    for i in range(len(lista)-1):
        lista.append(lista.pop(0))
        cadena = "".join(lista)
        
        rotaciones.append(cadena)
    
    return rotaciones

print(rotar("rotar"))

    
