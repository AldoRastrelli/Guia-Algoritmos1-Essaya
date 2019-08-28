MULTIPLICADOR = 60
DIVISOR = 60

def solicitar_datos():
	"""Solicita una cantidad de horas minutos y segundos al usuario"""

	h = float(input("Ingrese la cantidad de horas a convertir: "))
	m = float(input("Ingrese la cantidad de minutos a convertir: "))
	s = float(input("Ingrese la cantidad de segundos a convertir: "))
	return(h,m,s)

def conversion_de_datos(h,m,s):
	"""Con una cantidad de horas, minutos y segundos,calculo los segundos."""

	H = h * MULTIPLICADOR ** 2
	M = m * MULTIPLICADOR
	S = s

	return(H+M+S)

def conversion_de_segundos(s):
	"""Con una cantidad de segundos, calcula la cantidad de horas, minutos y segundos."""

	X = s // DIVISOR	

	H = (X) // DIVISOR
	M = (X) % DIVISOR
	S = (s % DIVISOR)

	return(H,M,S)

print("Primer intervalo")
h1,m1,s1 = solicitar_datos()
print("Segundo intervalo")
h2,m2,s2 = solicitar_datos()

seg_totales_1 = conversion_de_datos(h1,m1,s1)
seg_totales_2 = conversion_de_datos(h2,m2,s2)
seg_total = seg_totales_1 + seg_totales_2

H,M,S = conversion_de_segundos(seg_total)

print("la suma es")
print(H,"horas")
print(M,"minutos")
print(S,"segundos")
