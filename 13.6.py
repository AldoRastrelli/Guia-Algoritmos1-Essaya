def numero_triangular(n):

    if n == 1:
        return n
    
    if 1 < n:
        n += numero_triangular(n-1)
        return n

print(numero_triangular(16))
    