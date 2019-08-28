#Análisis
"""Necesito convertir grados Celcius ingresados por el usuario a Fahrenheit"""

#Especificación
"""Se le solicitará al usuario que ingrese el valor (flotante) de grados en Celcius y luego se imprimirá el valor en Fahrenheit"""

#Diseño
"""La función calcular_F(C) convertirá mis grados °C en F.

El programa imprimirá el pedido de un valor al usuario y luego imprimirá el valor convertido en F"""

def calcular_F(C):
	
	#El programa calcula el valor en Fahrenheit de 'C' grados °C
	return (9/5) * C + 32

print("El programa convierte un valor en °C a Fahrenheit")
C = float(input("Ingrese el valor de °C: "))

print(C,"grados Celcius =",calcular_F(C),"°F")
