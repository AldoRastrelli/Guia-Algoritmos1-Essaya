def como_juegan(lista,dic):

    dic_dep = {}

    for nombre in lista:
        dic_dep[nombre] = []

    for deporte in dic:
        
        for persona in dic[deporte]:

            if persona in dic_dep:

                tupla = (dic[deporte][persona],deporte)
                dic_dep[persona].append(tupla)

    return dic_dep

lista = ['Aldana','Ana','Luz']
dic = {'remo':{'Ana':100,'Luz':90}, 'tenis': {'Ana':50}}

print(como_juegan(lista,dic))