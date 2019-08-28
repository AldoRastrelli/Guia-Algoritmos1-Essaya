def calculo(base,altura):
	
	#Calcula el perímetro dados los datos solicitados en datos()
	return base * 2 + altura * 2

def datos():

	#interactúa con el usuario y solicita base y altura de un rectángulo, devolviendo su 		perímetro

	print("Cálculo del perímetro de un rectángulo")
	b=float(input("Indique la base del rectángulo: "))
	h=float(input("Indique la altura del rectángulo: "))
	Perímetro= calculo(b,h)
	print("El perímetro del rectángulo es",Perímetro)

datos()
