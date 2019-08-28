def recibir_datos():
	"""Recibe las coordenadas de un vector ingresadas por el usuario"""

	x = float(input("Ingrese la primer coordenada: "))
	y = float(input("Ingrese la segunda coordenada: "))
	z = float(input("Ingrese la tercer coordenada: "))

	return x,y,z

def devolver_norma(x,y,z):
	"""con los datos de las coordenadas del vector dado, calcula la norma"""

	N = round(( x ** 2 + y ** 2 + z ** 2 ) **0.5, 4)
	return N

print("El programa calcula la norma de un vector dado")
x, y, z = recibir_datos()
print("Norma=",devolver_norma(x,y,z))
