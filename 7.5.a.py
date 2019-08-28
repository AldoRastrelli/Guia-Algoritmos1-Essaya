def solicitar_lista_de_enteros():
    "solicita una lista con números enteros al usuario"
    
    lista = input("Ingrese una lista con números enteros: ").split(" ")

    while not verificar_enteros(lista):
        print("La lista debe tener únicamente números enteros.")
        lista = input("Ingrese una nueva lista: ").split(" ")

    return lista

def verificar_enteros(lista):
    "verifica que la lista tenga sólo números enteros"

    for x in lista:
        if not x.isdigit():
            if x != "" and x[0] == "-" and x[1:].isdigit():
                continue
            else:
                return False
        continue
    return True

def eliminar_no_primos(lista):
    "quita todos los números que no sean primos de la lista"

    for elem in lista:
        if not es_primo(int(elem)) or int(elem) < 0:
            lista.remove(elem)
    
    return lista

def es_primo(n):
	"Dado un número entero n, indica si es primo o no"

	for i in range(2,n):
		if n%i==0:	# % :: "módulo"	
			return False
		continue
	return True
      
print("El programa devuelve la lista sólo con los números primos")
lista = solicitar_lista_de_enteros()
print(eliminar_no_primos(lista))