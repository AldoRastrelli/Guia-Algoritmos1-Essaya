#Análisis
"""Necesito imprimir una tabla de conversión de grados Celcius a Fahrenheit"""

#Especificación
"""El programa no interactuará con el usuario. Sólo imprimirá la tabla de conversión, desde 0°F a 120°C, que salte de a 10°F"""

#Diseño
"""Definiré una variable F tal que pueda asignarle un range(0,121,10).
calcular_C(F) devolverá todos los valores de C correspondientes a F dentro del rango """

def calcular_C(F):
	
	#El programa calcula el valor en °C dado el valor de °F
	return round(((F - 32)*5/9),2)

print("Tabla de conversión de °F a °C:")

for F in range(0,121,10):
	
	#Se itera F entre 0 y 120, saltando de a 10 valores, y se imprime su conversión a °C
	print(F,"°F=",calcular_C(F),"°C")
