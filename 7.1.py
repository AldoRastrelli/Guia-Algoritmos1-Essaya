def recibir_tupla():
    "recibe una tupla de elementos"

    tupla = tuple(input("Ingrese elementos separados por un espacio: ").split(" "))

    return tupla

def menor_a_mayor(tupla):
    "ordena una tupla de menor a mayor"

    return tuple(sorted(tupla))

def esta_ordenada(tupla):
    "indica si la tupla está ordenada de menor a mayor"

    return tupla == menor_a_mayor(tupla):

print("El programa indica si una lista está ordenada de menor a mayor.")
tupla = recibir_tupla()
print(esta_ordenada(tupla))
