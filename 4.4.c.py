def fijar_variables():
	
	print("Primer recta:")
	m1,b1 = solicitar_datos()
	print("\nSegunda recta:")
	m2,b2 = solicitar_datos()

	return m1,b1,m2,b2

def solicitar_datos():
	"""Solicita al usuario la pendiente y la ordenada al orígen de una recta"""
	
	m = float(input("Ingrese la pendiente 'm': "))
	b = float(input("Ingrese la ordenada al origen 'b': "))

	return m,b

def pendientes_son_iguales(m1,m2):
	"""Verifica que las pendientes dadas por el usuario no sean la misma
	o múltiplos de sí misma"""

	return m1 == m2

def calcular_intersección(m1,b1,m2,b2):
	"""Calcula la intersección entre dos rectas"""

	x = (b2 - b1) / (m1 - m2)
	y = m1 * x + b1

	return x,y



print("El programa calcula la intersección entre dos rectas.\n")
print("Siendo la recta y = mx + b, 'm' la pendiente y 'b' la ordenada al origen.\n")

m1,b1,m2,b2 = fijar_variables()

while pendientes_son_iguales(m1,m2) == True:
	print("\nLas pendientes no pueden ser iguales.\n")
	m1,b1,m2,b2 = fijar_variables()

print("\nLa intersección de las dos rectas es el punto", calcular_intersección(m1,b1,m2,b2))






