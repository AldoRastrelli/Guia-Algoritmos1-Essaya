def obtener_combinaciones(N1,N2,N3,N4):
	
	M=0
	for i in (N1,N2,N3):
		for j in (N2,N3,N4):
			if i != j:
				M=max(M,i*j)
				
	return M
				
def solicitar_num():

	N1 = int(input("Ingrese un número: "))
	N2 = int(input("Ingrese un número: "))
	N3 = int(input("Ingrese un número: "))
	N4 = int(input("Ingrese un número: "))
	return N1,N2,N3,N4

N1,N2,N3,N4 = solicitar_num()
print(obtener_combinaciones(N1,N2,N3,N4))


