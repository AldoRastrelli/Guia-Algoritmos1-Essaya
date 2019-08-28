def solicitar_datos():
    "solicita un año al usuario"

    año = int(input("ingrese un año: "))
    return año

def convertir_a_romanos():
    "convierte el año a números romanos"

    año = solicitar_datos()

    unidades = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    simbolos = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    resultado = []
    for i in range(len(unidades)):
        cociente = int(año / unidades[i])
        resultado.append(simbolos[i] * cociente)
        año -= unidades[i] * cociente
    return ''.join(resultado)

print(convertir_a_romanos())