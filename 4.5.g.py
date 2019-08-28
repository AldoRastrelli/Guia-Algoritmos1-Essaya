from datetime import date
from dateutil import relativedelta #Requiere de instalación previa para su uso, buscar en stackoverflow

def diferencia_fechas():
    """Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indica el tiempo transcurrido
    entre ambas, en años, meses y días."""

    print('Primer fecha:')
    dia1, mes1, año1 = solicitar_datos()
    print('\nSegunda fecha:')
    dia2, mes2, año2 = solicitar_datos()

    fecha1 = date(año1,mes1,dia1)
    fecha2 = date(año2,mes2,dia2)
    diferencia = relativedelta.relativedelta(fecha2, fecha1)
    
    diferencia_años = diferencia.years
    diferencia_meses = diferencia.months
    diferencia_dias = diferencia.days

    return f'{diferencia_dias} dias, {diferencia_meses} meses y {diferencia_años} años entre {dia1}/{mes1}/{año1} y {dia2}/{mes2}/{año2}.'


def solicitar_datos():
    "solicita datos al usuario"

    dia = int(input("\nIngrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    while not fecha_es_valida(dia,mes,año):
        print('La fecha ingresada no es válida.')
        dia = int(input("\nIngrese el día: "))
        mes = int(input("Ingrese el mes: "))
        año = int(input("Ingrese el año: "))
    
    return dia, mes, año

def indicar_año_bisiesto(año):
    "indica si el año dado por el usuario es bisiesto"

    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    return False

def calcular_días_del_mes(mes,año):
    "Calcula la cantidad de días que tiene el mes ingresado"

    meses31 = (1,3,5,7,8,10,12)

    if mes == 2:
        if indicar_año_bisiesto(año) == True:
            return 29
        return 28
    if mes in meses31:
        return 31
    return 30

def fecha_es_valida(dia,mes,año):
    "indica si una fecha dada es válida"

    if mes <= 12 and mes > 0:
        if dia <= calcular_días_del_mes(mes,año) and dia > 0:
            if año > 0:
                return True
    return False

print(diferencia_fechas())