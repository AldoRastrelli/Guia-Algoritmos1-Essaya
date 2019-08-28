PASSWORD = "ABC"
from time import sleep

def solicitar_contraseña():

    pass_ingresada = input("Ingrese su contraseña: ")

    contador = 0
    while contador < 2 and pass_ingresada != PASSWORD:
            contador += 1
            sleep(3+contador)
            pass_ingresada = input("La contraseña ingresada es incorrecta. Intente nuevamente: ")
            
    
    if pass_ingresada == PASSWORD:
        print("Bienvenide")
    else:
        print("No more intentos, jaja salu3")

    

solicitar_contraseña()

