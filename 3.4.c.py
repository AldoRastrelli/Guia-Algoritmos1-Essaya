def recibir_datos():
	"""Recibe las coordenadas de un vector ingresadas por el usuario"""

	x = float(input("Ingrese la primer coordenada: "))
	y = float(input("Ingrese la segunda coordenada: "))
	z = float(input("Ingrese la tercer coordenada: "))

	return x,y,z

def devolver_productov(x1,x2,y1,y2,z1,z2):
	"""con las coordenadas de los vectores dados, calcula el producto vectorial y devuelve los resultados de las coordenadas del mismo"""

	X = y1 * z2 - z1 * y2
	Y = z1 * x2 - x1 * z2
	Z = x1 * y2 - y1 * x2 
	return X,Y,Z


print("El programa calcula el producto vectorial entre dos vectores dados.")

print("Primer vector:")
x1, y1, z1 = recibir_datos()
print("Segundo vector:")
x2, y2, z2 = recibir_datos()

print("El producto vectorial tiene coordenadas:","(X,Y,Z):",devolver_productov(x1,x2,y1,y2,z1,z2))
