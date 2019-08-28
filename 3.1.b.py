#Análisis 
"""El programa debe convertir segundos en horas, minutos y segundos."""

#Especificación
"""Se le solicitan segundos al usuario y por medio de una función, se convierten a horas, minutos y segundos"""

#Diseño
"""Por medio de s//60 //60 se calculan la cantidad de horas, (s//60)%60 la cantidad de minutos, y (s%60 serán los segundos"""

DIVISOR = 60

def conversion_de_segundos(s):
	"""Con una cantidad de segundos, calcula la cantidad de horas, minutos y segundos."""

	X = s // DIVISOR	

	H = (X) // DIVISOR
	M = (X) % DIVISOR
	S = (s % DIVISOR)

	return(H,M,S)

def solicitar_segundos():
	"""Solicita una cantidad de segundos al usuario"""

	s = float(input("Ingrese la cantidad de segundos a convertir: "))
	
	return(s)

s = solicitar_segundos()
H,M,S = conversion_de_segundos(s)

print(s, "segundos son:")
print(H,"horas")
print(M,"minutos")
print(S,"segundos")
