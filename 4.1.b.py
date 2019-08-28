def es_primo(n):
	#Dado un número entero n, indica si es primo o no

	for i in range(2,n):
		if n%i==0:	# % :: "módulo"	
			return "No es primo"
		continue
	return "Es primo"

def solicitar_numero():
	#Solicita un número al usuario

	n = int(input("Ingrese un número natural: "))
	return n

def es_primo_2(n): #Con 4 :: range(2,2) es un rango vacío. ¿Cómo arreglarlo?

	for i in range(2,n//2):
		if n % i == 0:
			return "false"
	return "true"


n = solicitar_numero()
print(es_primo(n))



