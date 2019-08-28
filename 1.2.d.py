from math import pi

def calcular_perimetro(radio):
	
	#Calcula el perímetro del círculo dado su radio
	return 2 * pi * radio

print("El siguiente programa calcula el perímetro de un círculo")
radio = float(input("Indique el radio del círculo: "))
perímetro = calcular_perimetro(radio)

print("El perímetro del círculo es",perímetro,)
