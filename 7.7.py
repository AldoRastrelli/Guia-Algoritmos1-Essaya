def nombre_inicial_punto_apellido(lista):
    "devuelve el nombre, inicial del segundo nombre, un punto y el apellido en forma de lista de cadenas"
    
    L = []
    for elemento in lista:
        L.append(f'{elemento[0]} {elemento[1][0].upper()}. {elemento[2]}')

    return L

lista = [('Aldana', 'Soledad', 'Rastrelli'),('Juan','Domingo','Perón')]
print(nombre_inicial_punto_apellido(lista))