def haGanado(tablero, jugador):
    for i in range(3):
        if tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador:
            return True
        if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
            return True

    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True

    return False

def main():
    # Inicializar el tablero vacío y los contadores
    tablero = []
    contA = 0
    contB = 0

    # Leer tres líneas de entrada
    for _ in range(3):
        linea = input().strip()
        tablero.append(list(linea))
        contA += linea.count('A')
        contB += linea.count('B')

    # Verificar si el número de fichas es válido
    if contA > contB + 1 or contB > contA:
        print("I")
        return

    # Verificar si A o B ha ganado
    aGano = haGanado(tablero, 'A')
    bGano = haGanado(tablero, 'B')

    # Validar condiciones de juego
    if aGano and bGano:
        print("I")
    elif aGano and contA == contB + 1:
        print("A")
    elif bGano and contA == contB:
        print("B")
    elif not aGano and not bGano and (contA + contB < 9):
        print("E")
    else:
        print("I")

if __name__ == '__main__':
    main()
