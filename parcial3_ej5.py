 """Escribir una función reducir que reciba por par ́ametro una cola y una funci ́on f de dos
par ́ametros, y aplique sucesivamente la funci ́on f a los dos primeros elementos de la cola (luego
de desencolarlos) y encole el resultado, hasta que solo quede un elemento. La funci ́on reducir
debe devolver el  ́unico elemento restante en la cola."""

def reducir(cola,funcion):

    if cola.esta_vacia():
        print('La cola está vacía.')
        return
    
    