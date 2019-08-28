def devolver_abs(n):
	#Devuelve el valor absoluto de un número n

	if n<0:
		return n*(-1)
	return n

def solicitar_numero():
	#Solicita un número al usuario

	n = int(input("Ingrese un número natural: "))
	return n

n = solicitar_numero()
print("El absoluto de",n,"es",devolver_abs(n))
