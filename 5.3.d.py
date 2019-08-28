PASSWORD = "ABC"
from time import sleep

def contraseña_correcta(pass_ingresada):
    "indica mediante un booleano si la contraseña ingresada es o no correcta"
    
    if pass_ingresada == PASSWORD:
        return True
    return False

def solicitar_contraseña():
    """solicita la contraseña hasta que se acaban los intentos o se introduce
    la contraseña correcta"""

    contador = 0
    verificacion=contraseña_correcta(input("Ingrese su contraseña: "))

    while contador < 2 and verificacion==False:
            contador += 1
            sleep(1+contador)
            verificacion=contraseña_correcta(input("La contraseña ingresada es incorrecta. Intente nuevamente: "))

    if verificacion == True:
        print("Bienvenide")
    else:
        print("No more intentos, jaja salu3")  

solicitar_contraseña()

