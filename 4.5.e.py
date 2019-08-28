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

def contador_dias(dia,mes,año):
    """cuenta los días que pasaron del año, verifica que el año sea o no bisiesto,
    y le resta a 365 o 366 respectivamente los días pasados."""
    
    contador = 0
    for i in range(1,mes):
        contador += calcular_días_del_mes(i,año)
    contador += dia

    if indicar_año_bisiesto(año):
        return 366 - contador
    return 365 - contador

print("\nEl programa calcula cuántos días faltan para terminar el año.")
dia,mes,año = solicitar_datos()

while not fecha_es_valida(dia,mes,año):
    print("\nLa fecha es inválida. Por favor, ingrese otra fecha.")
    dia, mes, año = solicitar_datos()

print(f"\nFaltan {contador_dias(dia,mes,año)} días para que termine el año {año}.")    
