#Análisis
"""El programa calcula el valor final a devolver de un préstamo, incluído el interés, de C cantidad de capital con x tasa de interés y n número de años para devolverlo. Debe poder interactuar con el usuario de una manera simple."""

#Especificación
"""EL programa solicitará 3 datos (C,x,n) y devolverá el valor final -valor a devolver del préstamo- según la función solicitada."""

#Diseño
"""La función calcular_deuda(C,x,n) devolverá el valor calculado según los datos ingresados y la función indicada.

Se le pedirá al usuario que ingrese las variables y luego se imprimirá el resultado con un mensaje."""



def calcular_deuda(C,x,n):

	#calcula con los datos ingresados por el usuario el dinero total a devolver por el préstamo
	return C * (1 + (x/100)) ** n

print ("Este programa calcula los intereses de un préstamo.")
C = float(input("Ingrese la cantidad de dinero: "))
x = float(input("Ingrese la tasa de interés: "))
n = int(input("Ingrese la cantidad de años: "))

print("El interés de su préstamo es", calcular_deuda(C,x,n))
