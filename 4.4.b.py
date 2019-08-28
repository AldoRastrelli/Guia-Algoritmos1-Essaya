j = (0 + 1j)

def solicitar_coef():
	#Solicita los coeficientes de un polinomio al usuario

	print("Siendo el polinomio de forma ax2 + bx + c")
	a = float(input("Ingrese el coeficiente 'a' del polinomio: "))
	b = float(input("Ingrese el coeficiente 'b' del polinomio: "))
	c = float(input("Ingrese el coeficiente 'c' del polinomio: "))
	return a,b,c


def validar_datos(a,b,c):
	#Valida los datos tal que las raíces obtenidas sean reales o se las tome como complejas

	
	x = b ** 2 - 4 * a * c
	if x<0:
		x = (-x)**0.5
		x= x * j
		
		return x
	return x**0.5



def devolver_raices(a,b,c,x):
	#Devuelve las raíces de un polinomio de la forma ax2+bx+c


	R1 = (-b + x)/ (2 * a)
	R2 = (-b - x)/ (2 * a)

	return R1,R2



print("El programa calcula las raíces de un polinomio dado.")
a,b,c = solicitar_coef()
x = validar_datos(a,b,c)
print(devolver_raices(a,b,c,x))

