
def obtener_combinaciones(N1,N2,N3,N4):

	MAX = N1* N2
	for i in (N1,N2,N3):
		for j in (N2,N3,N4):
			if i != j :
				MAX = max(MAX,i*j)
			
			
	print(MAX)

obtener_combinaciones(1,5,-2,-4)

#consulta


