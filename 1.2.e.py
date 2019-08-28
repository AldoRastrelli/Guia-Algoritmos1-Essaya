from math import pi

def calcular_area(radio):
	
	#Calcula el perímetro del círculo dado su radio
	return pi * radio ** 2

print("El siguiente programa calcula el área de un círculo")

radio = float(input("Indique el radio del círculo: "))
area = calcular_area(radio)

print("El área del círculo es",area)
