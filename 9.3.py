def consultar_nombre(nombre,agenda):
    """recibe un nombre del usuario. Si el nombre está en la agenda, devuelve el teléfono.
    De lo contrario, devuelve 0"""

    telefono  = buscar_telefono(nombre,agenda)
    if telefono  == 0:
        return 0
    else:
        return telefono
        
def buscar_telefono(nombre,agenda):
    """devuelve si el nombre está o no en la agenda. Si está, devuelve el teléfono asociado.
    De lo contrario, devuelve 0"""

    return agenda.get(nombre,0)

def modificar_agregar_telefono(nombre,telefono,agenda):
    """permite modificar el teléfono asociado al nombre pasado por parámetro"""

    agenda[nombre] = telefono

def main():

    agenda = {}
    nombre = input('Ingrese un nombre o * para salir: ')

    while nombre !=  '*' :
        
        if not consultar_nombre(nombre,agenda):
            print('El nombre buscado no se encuentra.')
            modificar_agregar_telefono(nombre,input('Ingrese el teléfono: '),agenda)
        
        else:
            print(f'{nombre}: {consultar_nombre(nombre,agenda)}')
            if input('¿Desea modificar el teléfono? ("Y" para modificar, cualquier otra tecla para seguir): ') == 'Y':
                modificar_agregar_telefono(nombre,input('Ingrese el nuevo teléfono: '),agenda)
            
        nombre = input('Ingrese un nombre o * para salir: ')

main()
            