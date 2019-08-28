"while"

i = 1
    
    while (m * i) < n:
        i += 1
    return (i - 1)

"for"

cont = 0
    for i in range(m,n):
        if i % m == 0 and i < n:
            cont += 1
    return cont

"""La función con while me resulta más clara por el hecho de que sin esforzarme
demasiado o sin conocimientos muy amplios, puedo entender qué está haciendo.
La función con while realiza muchas menos operaciones ya que compara
únicamente los múltiplo y no necesita verificar (como en el for) que i%m==0."""