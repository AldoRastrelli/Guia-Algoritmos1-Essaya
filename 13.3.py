def es_potencia(n,b):
    """Recibe dos enteros n y b y devuelve True si n es potencia de b."""

    if n == b or n == 1:
        print(f'DEBUG n = b ó n = 1. b: {b}, n: {n}')
        return True
    if b == 0 or n == 0:
        return False

    cociente = n / b
    print('DEBUG cociente = ',cociente)
    
    if n%b != 0:
        print('DEBUG el resto no es 0')
        return False

    elif cociente != 1:
            print('DEBUG cociente distinto de 1')
            return es_potencia(cociente, b)


print(es_potencia(1,451))
