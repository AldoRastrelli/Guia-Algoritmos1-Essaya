#Análisis
"""Necesito un programa que enumere todas las fichas del estilo dominó, con un juego cuyo valor máximo en un lado de la ficha es n"""

#Especificación
"""Necesito que el programa haga dos iteraciones de x1 y x2 números, con x1 entre 0 y n, y x2 entre 0 y n-1."""

#Diseño
"""La función iterar_lados(x1) iterará x1 y x2 dentro de los rangos especificados."""

def iterar_lados(n):
	
	for i in range(0 , n+1):
		for j in range(0 , i+1):
			print(i , "," , j)

n = int(input("Ingrese el máximo número que figura en las fichas del juego: "))

print("las fichas del juego son:")

iterar_lados(n)
