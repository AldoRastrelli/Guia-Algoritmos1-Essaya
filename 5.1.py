def promedio_notas():
    "solicita notas al usuario"
    
    suma = 0
    contador = 0

    while True:
        entrada = input("Ingrese una nota o pulse * para salir: ")
        if entrada == "":
            continue
        if entrada == "*":
            break
        n = float(entrada)
        suma += n
        contador += 1
        promedio = suma / contador
        print(f"Promedio: {promedio}")

promedio_notas()

