def hola(persona):
	"""Utilizo el nombre para saludar por pantalla"""
	print("Hola,",persona)


def preguntar():
	
	"""Solicito el nombre al usuario a partir de una pregunta"""
	
	nombre=input("Cuál es tu nombre? ")
	print( hola(nombre) )

preguntar()
