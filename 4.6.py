def calcular_dia_semana(n_dia):
	#Recibe un n-día del año entre 1 y 366 y devuelve qué día de la semana fue

	n_dia= n_dia % 7
	
	if n_dia == 0:
		return "Domingo"
	if n_dia == 1:
		return "Lunes"
	if n_dia == 2:
		return "Martes"
	if n_dia == 3:
		return "Miércoles"
	if n_dia == 4:
		return "Jueves"
	if n_dia == 5:
		return "Viernes"
	else:
		return "Sábado"

print(calcular_dia_semana(245))