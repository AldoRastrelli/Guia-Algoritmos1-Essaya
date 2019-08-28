def vote_por_mi(tupla):
    "recibe una tupla con nombres y por cada nombre, imprime un mensaje"

    for elem in tupla:
        print(f"Estimado/a {elem}, vote por el MLI.")
        #print(f"Estimado/a {elem}, vote por mí.")

tupla = ("alumno/a fiubense","estudiante de Ingeniería")
vote_por_mi(tupla)