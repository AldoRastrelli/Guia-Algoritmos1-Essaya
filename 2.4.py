#Análisis
"""Se quieren imprimir números pares dentro de un rango que dé el usuario"""

#Especificación
"""Se solicitarán dos números al usuario, enteros para mayor facilidad, y el programa imprimirá todos los números pares dentro de dicho rango"""

#Diseño
"""La función calcular_inicio(x,y) decidirá si empezar por x o x+1 según el resto de x/2 sea 0 o 1 (o sea, según x sea par o impar).
La función calcular_pares(x,y) calculará los números pares según el inicio indicado en calcular_inicio por medio de un range(x',y',2) y los imprimirá.
Se le solicitará al usuario que ingrese x e y"""

def calcular_pares(x,y):

	for p in range(x,y,2):
		print(p)

def calcular_inicio(x,y):
		
	if (x%2==0):
		return calcular_pares(x,y+1)

	return calcular_pares(x+1,y+1)

print("El programa muestra todos los números pares dentro de un rango ingresado [x,y]")
x = int(input("Indique X: "))
y = int(input("Indique Y: "))

calcular_inicio(x,y)


