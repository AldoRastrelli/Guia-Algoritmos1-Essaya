from random import randrange
minim= 0
maxim=50
x = randrange(minim,maxim)

def adivinar_número(x):
    """Deja al usuario adivinar el número x, indicando si es más grande
    o más chico de lo indicado"""

    while True:
        guess = int(input(f"Adivine el número X, del {minim} al {maxim}: "))
        if guess<x:
            print(f"X es más grande que {guess}")
            continue
        if guess>x:
            print(f"X es más pequeño que {guess}")
            continue
        else:
            break
    print(f"Adivinaste!")

adivinar_número(x)