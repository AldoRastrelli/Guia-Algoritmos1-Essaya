from cola import Cola()

def promedio_espera(lista_eventos):

    personas, colectivos = encolar_personas_enlistas_colectivos
    cantidad_personas = contar_personas()
    suma_espera = subir_personas(personas,colectivos)

def encolar_personas_enlistas_colectivos(lista_eventos):

    personas = Cola()
    colectivos = []

    for evento in lista_eventos:
        if evento[1] == 'p':
            personas.encolar(evento)
        else:
            colectivos.append(evento)
    
    return personas, colectivos

def contar_personas(personas)):

        if personas.esta_vacia():
            return 0

        i = 1
        cola_aux = Cola()
        while not personas.esta_vacia():
            cola_aux.encolar(personas.desencolar())
            i +=1
        
        while not cola_aux.esta_vacia():
            personas.encolar(cola_aux.desencolar())

        return i

def subir_personas(personas,colectivos):

    suma = 0

    for bondi in colectivos:
        capacidad = bondi[2]
        tiempo_llegada_bondi = bondi[0]

        while capacidad > 0:
            
            if pila.esta_vacia():
                return suma

            tiempo_llegada_persona = personas.desencolar()[1]

            if tiempo_llegada_bondi >= tiempo_llegada_persona:

                suma += tiempo_llegada_bondi - tiempo_llegada_persona
                capacidad -= 1
            else:
                
                break
    
    return suma
    