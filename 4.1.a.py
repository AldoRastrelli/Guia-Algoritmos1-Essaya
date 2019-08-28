def es_par(n):
	#Dado un número entero n, indica si es par o no

	if n%2==0:
		return "Es par"
	return "No es par"

def solicitar_numero():
	#Solicita un número al usuario

	n = int(input("Ingrese un número natural: "))
	return n

n = solicitar_numero()
print(es_par(n))

