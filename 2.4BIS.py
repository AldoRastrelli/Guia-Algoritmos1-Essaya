
def calcular_pares(x,y):

	for p in range(x,y,2):
		print(p)

def calcular_inicio(x,y):
		
	if (x%2):
	#Si x%2==0, x es par.
	#Pyhton lee "0==False" [todo 0 es FALSE, todo !=0 es TRUE].
	#Procedo con acción de "si x es impar"
		return calcular_pares(x+1,y+1)

	return calcular_pares(x,y+1)

print("El programa muestra todos los números pares dentro de un rango ingresado [x,y]")
x = int(input("Indique X: "))
y = int(input("Indique Y: "))

calcular_inicio(x,y)


