def producto_de_matrices(m1,m2):
    "devuelve el producto de dos matrices"
    
    
    S = [[ m1[i][j]*m2[i][j] for j in range(len(m1)) ] for i in range(len(m1[0])) ]
    
    return S

m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[1,2,3],[4,5,6],[7,8,9]]
print(producto_de_matrices(m1,m2))