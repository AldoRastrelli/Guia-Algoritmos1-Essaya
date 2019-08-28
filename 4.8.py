MESES = 'enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre'
MESES31= 'enero, marzo, mayo, julio, agosto, octubre, diciembre'

def signo_zodiaco():
    """el usuario ingresa el día y mes de su cumpleaños
    y el programa le dice a qué signo corresponde."""

    dia, mes = pedir_cumpleaños()

    if (mes == 'marzo' and dia >= 21) or (mes == 'abril' and dia <= 20):
        return 'Aries'
    elif (mes == 'abril' and dia >= 21) or (mes == 'mayo' and dia <= 20):
        return 'Tauro'
    elif (mes == 'mayo' and dia >= 21) or (mes == 'junio' and dia <= 20):
        return 'Géminis'
    elif (mes == 'junio' and dia >= 21) or (mes == 'julio' and dia <= 20):
        return 'Cáncer'
    elif (mes == 'julio' and dia >= 21) or (mes == 'agosto' and dia <= 20):
        return 'Leo'
    elif (mes == 'agosto' and dia >= 21) or (mes == 'septiembre' and dia <= 20):
        return 'Virgo'
    elif (mes == 'septiembre' and dia >= 21) or (mes == 'octubre' and dia <= 20):
        return 'Libra'
    elif (mes == 'octubre' and dia >= 21) or (mes == 'noviembre' and dia <= 20):
        return 'Escopio'
    elif (mes == 'noviembre' and dia >= 21) or (mes == 'diciembre' and dia <= 20):
        return 'Sagitario'
    elif (mes == 'diciembre' and dia >= 21) or (mes == 'enero' and dia <= 20):
        return 'Capricornio'
    elif (mes == 'enero' and dia >= 21) or (mes == 'febrero' and dia <= 20):
        return 'Acuario'
    else:
        return 'Piscis'

def pedir_cumpleaños():

    mes = input('Ingrese el mes en el que cumple años: ')

    while mes.lower() not in MESES:
        print('Mes no válido.')
        mes = input('Ingrese el mes en el que cumple años: ')

    dia = int(input('Ingrese el día en el que cumple años: '))

    while not (0 < dia <= calcular_días_posibles_del_mes(mes)):

        print('El día ingresado no es válido')
        dia = int(input('Ingrese el día en el que cumple años: '))
    
    return dia, mes

def calcular_días_posibles_del_mes(mes):
    "Calcula la cantidad de días que tiene el mes ingresado"

    if mes.lower() == 'febrero':
        return 29
    if mes.lower() in MESES31:
        return 31
    else:
        return 30

print(signo_zodiaco())