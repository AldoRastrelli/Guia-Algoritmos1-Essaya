def coord(a,b):

	#Convierto las coordenadas en las normas de los lados

	return abs(a - b)
	
def area(base,altura):

	#Calculo el área a partir de las normas de la base y la altura
	return base * altura

def programa():

	#Solicita coordenadas de vértices opuestos del rectángulo al usuario y luego calcula el área.
	
	x1 = float(input("Indique la coordenada x1: "))
	y1 = float(input("Indique la coordenada y1: "))
	print("La coordenada ingresada es (",x1,",",y1,")")

	x2 = float(input("Indique la coordenada x2: "))
	y2 = float(input("Indique la coordenada y2: "))
	print("La coordenada ingresada es (",x2,",",y2,")")


	base = coord(x1,x2)
	altura = coord(y1,y2)
	resultado = area(base,altura)
	return (resultado)
	
	#print("el área es",area(coord(x1,x2),coord(y1,y2)))


print ("El área es",programa())
	

	

