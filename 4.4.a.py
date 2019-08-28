def polinomio(x):
	#calcula el valor del polinomio evaluado en x

	return a * x **2 + b * x + c

def devolver_max_o_min(a,b,c):
	#Dados los 3 coeficientes de un polinomio de segundo grado, calcula los puntos máximos y mínimos.

	x = -b / (2*a)
	p = 2 * a * x

	if p>0:
		print(x,"es punto máximo y vale", polinomio(x))
	elif p==0:
		if a>0:
			print(x,"es punto mínimo y vale", polinomio(x))
		print(x,"es punto máximo y vale", polinomio(x))
	else:
		print(x,"es punto mínimo y vale", polinomio(x))

def solicitar_coef():
	#Solicita un número al usuario

	print("Siendo el polinomio de forma ax2 + bx + c")
	a = float(input("Ingrese el coeficiente 'a' del polinomio: "))
	b = float(input("Ingrese el coeficiente 'b' del polinomio: "))
	c = float(input("Ingrese el coeficiente 'c' del polinomio: "))
	return a,b,c

a,b,c = solicitar_coef()
devolver_max_o_min(a,b,c)
