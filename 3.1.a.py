#Análisis 
"""El programa debe convertir de horas, minutos y segundos; a segundos."""

#Especificación
"""Se le solicitanlos datos al usuario y por medio de una función, se convierten en segundos"""

#Diseño
"""las horas se las multiplicará por 3600, los minutos por 60 y los segundos se sumarán"""

MULTIPLICADOR = 60

def conversion_de_datos(h,m,s):
	"""Con una cantidad de horas, minutos y segundos,calculo los segundos."""

	H = h * MULTIPLICADOR ** 2
	M = m * MULTIPLICADOR
	S = s

	return(H+M+S)

def solicitar_datos():
	"""Solicita una cantidad de horas minutos y segundos al usuario"""

	h = float(input("Ingrese la cantidad de horas a convertir: "))
	m = float(input("Ingrese la cantidad de minutos a convertir: "))
	s = float(input("Ingrese la cantidad de segundos a convertir: "))
	return(h,m,s)

h,m,s = solicitar_datos()
suma = conversion_de_datos(h,m,s)

print("El total es:")
print(suma,"segundos.")
