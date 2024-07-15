def Posicion (K):
    posicion = (K - 1) % 10
    if (posicion == 0):
        return 1
    elif (posicion == 1):
        return 4
    elif (posicion == 2):
        return 1
    elif (posicion == 3):
        return 5
    elif (posicion == 4):
        return 9
    elif (posicion == 5):
        return 2
    elif (posicion == 6):
        return 6
    elif (posicion == 7):
        return 5
    elif (posicion == 8):
        return 3
    else:
        return 5

K = int(input())

print(Posicion(K))