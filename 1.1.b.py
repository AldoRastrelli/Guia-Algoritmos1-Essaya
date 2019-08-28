def producto(a,b):

	#multiplica a y b
	return a * b

def ask():

	#interactúa con el usuario solicitando los números a multiplicar entre sí y devolviendo la respuesta

	print("Este programa multiplica dos números")

	a=float(input("Inserte el primer número: "))
	b=float(input("Inserte el segundo número: "))
	P= producto(a,b)

	print("El producto entre ",a," y ",b," es ",P)
ask()
