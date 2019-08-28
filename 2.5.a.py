#Análisis
"""Me piden imprimir una secuencia de numeros en un rango de [1,n], n solicitada al usuario, tal que se lea n y "número triangular de n"."""

#Especificación
"""Se solicita un número al usuario. Ese número será el tope del range.
Se calculará el número triangular correspondiente a cada iteración entre el rango [1,n] y se imprimirá cada par (n, número triangular de n)."""

#Diseño
"""La función calcular_t(x) utilizará un i in range(1,x+1) para calcular el número T (triangular) a cada i perteneciente al rango. Se imprimirán pares de resultado (i,t)"""


def calcular_t(x):
	
	#Calcula en forma de serie los números triangulares
	t=0
	for i in range(1,x+1):
		t=t+i
		# t+=i
		print(i,"-",t)

x=int(input("Ingrese el tope del rango a calcular: "))

calcular_t(x)

#SPOILER ALERT: Esta opción entre ambos ítems (a y b) es la que requiere menos código y de manera más sencilla.
