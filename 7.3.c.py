def mensaje_en_rango(tupla,p,n):
    """recibe una tupla con nombres e imprime un mensaje
    para los n nombres que se encuentran desde la posición p,
    dependiendo de si son de la carrera o del CBC"""

    for i in range(p,p+n):
        if tupla[i][1] == "carrera" :
            print(f"Estimado/a {tupla[i][0]}, vote por el MLI.")
        else:
            print(f"Estimado/a {tupla[i][0]}, si usted aprobó dos materias del CBC, puede votar. Vote por el MLI.")
        #print(f"Estimado/a {tupla[i]}, vote por mí.")

tupla = (("Aldana", "carrera"), ("Nicolás", "carrera"), ("Lucía","CBC"), ("Miroslav","carrera"),("Lautaro","CBC"))
mensaje_en_rango(tupla,1,3)