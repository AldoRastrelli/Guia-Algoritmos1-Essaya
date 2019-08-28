def buscar_en_agenda(input_usuario,agenda):
    """recibe una cadena a buscar y una lista de tuplas (nombre_completo,teléfono)
    y busca dentro de la lista todas las entradas que contienen en el nombre completo
    la cadena recibida. Devuelve una lista con todas las tuplas encontradas"""

    return [agenda[i] for i in range(len(agenda)) if input_usuario in agenda[i][0]]

print(buscar_en_agenda('Olga',[('Romero, Olga',123),('Parrilla Gómez, Analía',456),('Pérez,Martín',789),('Martinez Parrilla',100)]))