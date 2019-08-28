MESES31= (1,3,5,7,8,10,12)

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

    if mes == 2:
        if indicar_año_bisiesto(año) == True:
            return 29
        return 28
    if mes in MESES31:
        return 31
    else:
        return 30


print("\nEl programa calcula la cantidad de meses que tiene un año indicado.")
año=int(input("Indique el año calendario: "))
mes=int(input("Indique el mes: "))

print(f"El mes {mes} del año {año} tiene {calcular_días_del_mes(mes,año)} días")


        