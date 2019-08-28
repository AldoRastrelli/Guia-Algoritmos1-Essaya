PASSWORD = "ABC"

def solicitar_contraseña(PASSWORD):

    pass_ingresada = input("Ingrese su contraseña: ")

    while pass_ingresada != PASSWORD:

    	pass_ingresada = input("La contraseña ingresada es incorrecta. Intente nuevamente: ")

    print("Bienvenide")

solicitar_contraseña(PASSWORD)