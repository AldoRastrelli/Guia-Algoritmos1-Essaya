"""8) Escribir una funci ́on recursiva que reciba una cadena y devuelva True si es un palındromo
(se lee igual hacia adelante que hacia atr ́as) o False si no lo es."""

def es_palindromo(cadena):

    cadena = "".join(cadena.split())
    print(cadena)
    print(revertir(cadena))
    return cadena.lower() == revertir(cadena).lower()

def revertir(cadena,reverso = ""):

    if not cadena:
        return cadena
    
    reverso = revertir(cadena[1:])
    if cadena[0] != " ":
        reverso += cadena[0]
    return reverso

print(es_palindromo("anita lava la tina"))    