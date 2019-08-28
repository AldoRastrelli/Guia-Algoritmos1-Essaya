def devolver_matriz(n):
	#Devuelve la identidad de la matriz de dimensión nxn

	if n<=0:
		print("La dimensión debe ser un número positivo mayor a 0")
	else:
		for i in range(1,n+1):
			print(" 0"*(i-1),"1","0 "*(n-i),"\n",)



def solicitar_numero():
	#Solicita un número al usuario

	n = int(input("Ingrese una dimensión: "))
	return n

n = solicitar_numero()
devolver_matriz(n)
