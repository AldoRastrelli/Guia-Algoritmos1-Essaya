from math import pi

def calcular_volumen(radio):

	#Calcula el volumen de una esfera dado su radio
	return 4/3 * pi * radio **3

print("El siguiente programa calcula el volumen de una esfera dado su radio.")

radio = float(input("Indique el radio de la esfera: "))
volumen = calcular_volumen(radio)

print ("El volumen de la esfera es",volumen)
