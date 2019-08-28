def solicitar_datos():
    "solicita datos al usuario"

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

print("\nEl programa calcula cuántos días faltan para terminar el mes.")
dia,mes,año = solicitar_datos()

while fecha_es_valida(dia,mes,año) == False:
    print("\nLa fecha es inválida. Por favor, ingrese otra fecha.")
    dia, mes, año = solicitar_datos()

print(f"\nFaltan {calcular_días_del_mes(mes,año) - dia} días para que termine el mes.")    
