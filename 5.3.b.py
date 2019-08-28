PASSWORD = "ABC"

def solicitar_contraseña():

    pass_ingresada = input("Ingrese su contraseña: ")

    contador = 0
    while contador < 2 and pass_ingresada != PASSWORD:
            pass_ingresada = input("La contraseña ingresada es incorrecta. Intente nuevamente: ")
            contador += 1
    
    if pass_ingresada == PASSWORD:
        print("Bienvenide")
    else:
        print("No more intentos, jaja salu3")

    

solicitar_contraseña()

