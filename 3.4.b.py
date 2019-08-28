def recibir_datos():
	"""Recibe las coordenadas de un vector ingresadas por el usuario"""

	x = float(input("Ingrese la primer coordenada: "))
	y = float(input("Ingrese la segunda coordenada: "))
	z = float(input("Ingrese la tercer coordenada: "))

	return x,y,z

def devolver_diferencia(x1,x2,y1,y2,z1,z2):
	"""con las coordenadas de los vectores dados, calcula coordenada a coordenada la diferencia y devuelve los resultados"""

	X = x1 - x2
	Y = y1 - y2
	Z = z1 - z2
	return X,Y,Z


print("El programa calcula las coordenadas del vector diferencia entre dos vectores dados.")

print("Primer vector:")
x1, y1, z1 = recibir_datos()
print("Segundo vector:")
x2, y2, z2 = recibir_datos()

print("El vector diferencia tiene coordenadas:","(X,Y,Z):",devolver_diferencia(x1,x2,y1,y2,z1,z2))
