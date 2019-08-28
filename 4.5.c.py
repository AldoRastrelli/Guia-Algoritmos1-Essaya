def indicar_año_bisiesto(año):
    "indica si el año dado por el usuario es bisiesto"

    if año % 400 == 0:
        return True
    if año % 100 == 0:
        return False
    if año % 4 == 0:
        return True
    return False

meses31= (1,3,5,7,8,10,12)

def calcular_días_del_mes(mes,año):
    "Calcula la cantidad de días que tiene el mes ingresado"

    if mes == 2:
        if indicar_año_bisiesto(año) == True:
            return 29
        return 28
    if mes in meses31:
        return 31
    else:
        return 30

def fecha_es_valida(dia,mes,año):
    "indica si una fecha dada es válida"

    if mes <= 12 and mes > 0:
        if dia <= calcular_días_del_mes(mes,año) and dia > 0:
            if año > 0:
                return "válida"
    return "inválida"

print("\nEl programa calcula si una fecha es válida.")

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

print(f"La fecha {dia}/{mes}/{año} es {fecha_es_valida(dia,mes,año)}.")