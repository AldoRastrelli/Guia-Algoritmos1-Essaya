def domino_encajan(a,b):
    "indica si dos fichas de domino encajan entre sí"

    ficha1 = list(a.split("-"))
    ficha2 = list(b.split("-"))
    
    for elem1 in ficha1:
        for elem2 in ficha2:
            if elem1 == elem2:
                return True
    return False

assert domino_encajan("3-4","5-4") == True
assert domino_encajan("3-4","5-2") == False