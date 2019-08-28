def pedir_entero(mensaje,minimo,maximo):
  """imprime un mensaje solicitando un número y lo devuelve únicamente si el número
  se encuentra entre el min y el máx"""

  x = input(f"\n{mensaje}: ")
    
  while not validar_input(mensaje,minimo,maximo,x):
    print(f"Por favor ingresa un número entre {minimo} y {maximo}")
    x = input(f"\n{mensaje}: ")
    continue

  return x

def validar_input(mensaje,minimo,maximo,x):
  """Valida que el valor de x sea entero y esté entre el minimo y el máximo.
  De ser así, devuelve x. De lo contrario, solicita otro número hasta que verifique
  y lo devuelve."""

  if not x.isdigit():

    if x == "": #si X es vacío (enter), devuelve falso
      return False

    if x[0] == "-" and x[1:].isdigit(): #si X empieza con "-" y los demás caracteres son digit
      return minimo <= int(x) <= maximo
    else:
      return False

  return minimo <= int(x) <= maximo #devuelve True or False si está entre min y max



#print(pedir_entero('Cuánto tenés en tu cuenta bancaria?',-150,150))
