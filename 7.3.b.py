def mensaje_en_rango(tupla,p,n):
    "recibe una tupla con nombres e imprime un mensaje para los n nombres que se encuentran desde la posición p"

    for i in range(p,p+n):
        print(f"Estimado/a {tupla[i]}, vote por el MLI.")
        #print(f"Estimado/a {tupla[i]}, vote por mí.")

tupla = ("Aldana", "Nicolas", "Miroslav", "Romina", "Juan", "Lautaro", "Elika", "Casimiro")
mensaje_en_rango(tupla,2,4)