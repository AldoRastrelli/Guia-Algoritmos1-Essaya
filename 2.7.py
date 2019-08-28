#Análisis
"""Necesito un programa que enumere todas las fichas de dominó"""

#Especificación
"""Necesito que el programa haga dos iteraciones de x1 y x2 números, con x1 entre 0 y 6, y x2 entre 0 y x1-1."""

#Diseño
"""La función iterar_lados(x1) iterará x1 y x2 dentro de los rangos especificados."""

def iterar_lados(x1):
	
	for i in range(0,x1+1):
		for j in range(0,i+1):
			print(i,",",j)

print("Fichas del dominó")

iterar_lados(6)
