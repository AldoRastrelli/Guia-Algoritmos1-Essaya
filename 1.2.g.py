def calcular_hip(c1,c2):

	#Calcular la hipotenusa de un triángulo rectángulo a partir de sus catetos

	return (c1**2+c2**2)**0.5

print("El siguiente programa calcula la hipotenusa de un triángulo rectángulo a partir de sus catetos.")

c1=float(input("Ingrese el valor del primer cateto: "))
c2=float(input("Ingrese el valor del segundo cateto: "))

print("El valor de la hipotenusa es",calcular_hip(c1,c2))
