#Análisis
"""Me piden imprimir una secuencia de numeros en un rango de [1,n], n solicitada al usuario, tal que se lea n y "número triangular de n", utilizando función dada."""

#Especificación
"""Se solicita un número al usuario. Ese número será el tope del range y se lo llamará n.
Se calculará el número triangular correspondiente a cada iteración entre el rango [1,n] y se imprimirá cada par (número, triangular del número)."""

#Diseño
"""La función calcular_t(x) utilizará un x in range(1,n+1) para calcular el número i (triangular) a cada x perteneciente al rango, usando la función dada. Se imprimirán pares de resultado (x,i)"""


def calcular_t(n):
	
	for x in range(1,n+1):		
		i = x * (x+1)/2
		print(x,"-",i)

n=int(input("Ingrese un número entero para utilizar de tope en el rango: "))

calcular_t(n)

#Esta opción entre ambos ítems (a y b) es la que requiere más código y de manera más compleja.
