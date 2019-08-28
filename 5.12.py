def dato_es_valido(n):
    "Indica si el valor ingresado es un digito o '-1' (True). Otra cosa (False)"

    return n.isdigit() or n == "-1"
    #3       (T          or   F)  = T  
    #H        (F          or   F) = F  
    #-1       (F          or   T) = T  

def dato_en_rango(n,EJ_TOTALES):
    "Me indica si mi numero n es menor o igual a mi cantidad de ejercicios totales"

    return float(n) <= EJ_TOTALES #TRUE , FALSE

def solicitar_datos():
    "Solicita al usuario datos que cumplan las condiciones pedidas (digit o '-1')"

    n = input("\nPara corregir un examen, ingrese la cantidad de ejercicios aprobados;\no '-1' para salir: ")
    
    while not dato_es_valido(n) or not dato_en_rango(n,EJ_TOTALES): #not TRUE = False = no entra
        print("\nEl dato ingresado no es válido.")
        n = input("Para corregir un examen, ingrese la cantidad de ejercicios aprobados;\no '-1' para salir: ")
    return n

EJ_TOTALES = 10

def calcular_porcentaje_aprobado():
    """calcula, dado la cantidad de ejercicios bien resueltos, el porcentaje aprobación
    e indica si el alumno aprobó o no (>60%)"""

    
    n = solicitar_datos()
    while n.isdigit():
        porcentaje = (float(n) / EJ_TOTALES) * 100
        if porcentaje >= 60:
            print(f"\nAPROBADO, {porcentaje}%")
        else:
            print(f"\nDESAPROBADO, {porcentaje}%")
        n = solicitar_datos()

print(f"\nLa cantidad de ejercicios totales en el examen es {EJ_TOTALES}.")
calcular_porcentaje_aprobado()
