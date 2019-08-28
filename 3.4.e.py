def recibir_datos():
	"""Recibe las coordenadas de un vector ingresadas por el usuario"""

	x = float(input("Ingrese la primer coordenada: "))
	y = float(input("Ingrese la segunda coordenada: "))
	z = 0

	return x,y,z


def devolver_diferencia(x1,x2,y1,y2,z1,z2):
	"""con las coordenadas de los vectores dados, calcula coordenada a coordenada la diferencia y devuelve los resultados"""

	X = x1 - x2
	Y = y1 - y2
	Z = z1 - z2
	return X,Y,Z


def devolver_productov(x1,x2,y1,y2,z1,z2):
	"""con las coordenadas de los vectores dados, calcula el producto vectorial y devuelve los resultados de las coordenadas del mismo"""

	X = y1 * z2 - z1 * y2
	Y = z1 * x2 - x1 * z2
	Z = x1 * y2 - y1 * x2 
	return X,Y,Z

def devolver_norma(x,y,z):
	"""con los datos de las coordenadas del vector dado, calcula la norma"""

	N = round(( x ** 2 + y ** 2 + z ** 2 ) **0.5, 4)
	return N



print("El programa calcula el área de un cuadrilátero convexo dado por cuatro puntos.","Se solicta al usuario ingresar los puntos de manera HORARIA, leyéndose los mismos: ABCD",sep="\n")

print("Primer punto, A:")
x1, y1, z1 = recibir_datos() #A
print("Segundo punto, B:")
x2, y2, z2 = recibir_datos() #B
print("Tercer punto, C:")
x3, y3, z3 = recibir_datos() #C
print("Cuarto puntO, D:")
x4, y4, z4 = recibir_datos() #D

d1,d2,d3 = devolver_diferencia(x1,x3,y1,y3,z1,z3) #A - C : diagonal del cuadrilátero
v1,v2,v3 = devolver_diferencia(x1,x2,y1,y2,z1,z2) #A - B
u1,u2,u3 = devolver_diferencia(x1,x4,y1,y4,z1,z4) #A - D

"""El área de un triángulo ABC se puede calcular como |AB x AC| / 2 """ 

w1,w2,w3 = devolver_productov(v1,d1,v2,d2,v3,d3) #producto vectorial de AB x AC
p1,p2,p3 = devolver_productov(u1,d1,u2,d2,u3,d3) #producto vectorial de AD x AC

print("El área del triángulo es:",devolver_norma(w1,w2,w3)/2 + devolver_norma(p1,p2,p3)/2)







