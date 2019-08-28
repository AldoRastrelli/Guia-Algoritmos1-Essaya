def calculo(b,h):
	
	#Calcula el área dados los datos solicitados en datos()
	return b* h

def datos():

	#interactúa con el usuario y solicita base y altura de un rectángulo, devolviendo su 		perímetro

	print("Cálculo del área de un rectángulo")
	b=float(input("Indique la base del rectángulo: "))
	h=float(input("Indique la altura del rectángulo: "))
	Perímetro= calculo(b,h)
	print("El área del rectángulo es",Perímetro)

datos()
