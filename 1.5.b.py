def multiplicar(n,m):
	
	#Crea la tabla de multiplicar, con un rango de 0 a 10

	return n * m

n=int(input("Indique un numero: "))

for m in range(11):
	print(n,"x",m,"=",multiplicar(n,m))
