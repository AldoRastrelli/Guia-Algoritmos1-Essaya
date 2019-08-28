def cantidad_digitos(n, cantidad = 0):
    """recibe un número positivo n y devuelve, por recursión, la cantidad de dígitos que tiene"""

    if not n:
        return cantidad
    
    return cantidad_digitos(str(n)[1:],cantidad+1)

print(cantidad_digitos(123456))

    
        
