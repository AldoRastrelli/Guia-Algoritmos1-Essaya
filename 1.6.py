def printear_mil_veces(palabra):
	
	for i in range (1001):

		print(palabra,end='')


palabra = str(input("Ingrese una palabra: "))

printear_mil_veces(palabra)

#el agregado de "end=''" indica que luego de terminar nuestra palabra, le seguirá lo que sea que hayamos indicado, para luego volver a imprimir nuestra palabra las veces que lo hemos solicitado con el range.
