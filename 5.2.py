def solicitar_numero():
	#Solicita un número al usuario

	n = int(input("Ingrese un número natural: "))
	return n

def descomponer_en_primos(n):
    #descompone el número en primos

    res = ""
    for contador in range(2,n):    

            if es_primo(contador) and n%contador==0:

                while n%contador==0:
                    res += str(contador) + " "
                    n = n//contador          
    return res

def es_primo(contador):
	#Dado un número entero "contador", indica si es primo o no

	for i in range(2,contador):
		if contador%i==0:	# % :: "módulo"	
			return False
	return True

n = solicitar_numero()
res = descomponer_en_primos(n)
print(res)
    

