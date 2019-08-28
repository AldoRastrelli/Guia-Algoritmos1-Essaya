def recibir_datos():
	"""Recibe las coordenadas de un vector ingresadas por el usuario"""

	x = float(input("Ingrese la primer coordenada: "))
	y = float(input("Ingrese la segunda coordenada: "))
	z = float(input("Ingrese la tercer coordenada: "))

	return x,y,z


def calcular_diferencia(x1,x2,y1,y2,z1,z2):
	"""con las coordenadas de los vectores dados, calcula coordenada a coordenada la diferencia y devuelve los resultados"""

	X = x1 - x2
	Y = y1 - y2
	Z = z1 - z2
	return X,Y,Z


def calcular_productov(x1,x2,y1,y2,z1,z2):
	"""con las coordenadas de los vectores dados, calcula el producto vectorial y devuelve los resultados de las coordenadas del mismo"""

	X = y1 * z2 - z1 * y2
	Y = z1 * x2 - x1 * z2
	Z = x1 * y2 - y1 * x2 
	return X,Y,Z

def calcular_norma(x,y,z):
	"""con los datos de las coordenadas del vector dado, calcula la norma"""

	N = round(( x ** 2 + y ** 2 + z ** 2 ) **0.5, 4)
	return N



print("El programa calcula el área de un triángulo en R3 dado por tres puntos.")

print("Primer punto:")
x1, y1, z1 = recibir_datos() #A
print("Segundo punto:")
x2, y2, z2 = recibir_datos() #B
print("Tercer punto:")
x3, y3, z3 = recibir_datos() #C

"""El área de un triángulo ABC se puede calcular como |AB x AC| / 2 """ 

v1,v2,v3 = calcular_diferencia(x1,x2,y1,y2,z1,z2) #A - B
u1,u2,u3 = calcular_diferencia(x1,x3,y1,y3,z1,z3) #A - C

w1,w2,w3 = calcular_productov(v1,u1,v2,u2,v3,u3) #producto vectorial de AB x AC

print("El área del triángulo es:",calcular_norma(w1,w2,w3)/2)







