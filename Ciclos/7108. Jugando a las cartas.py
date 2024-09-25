def main():
    
    N, M = map(int,input().split())
    partidas = []
    
    for i in range(N):
        entrada = list(map(int, input().split()))
        partidas.append(entrada)
        
    dineroJugador = M
    
    for i in range(N):
        B, *cartas = partidas[i]
        puntosJugador = 0
        carta = 0
        
        while puntosJugador < 16 and carta < 10:
            puntosJugador += cartas[carta]
            carta += 1
            if puntosJugador >= 21:
                break
            
        puntosCasa = 0
        if puntosJugador <= 21:
            while puntosCasa < puntosJugador and carta < 10:
                puntosCasa += cartas[carta]
                carta += 1
                if puntosCasa >= 21:
                    break
                
        if puntosJugador > 21:
            print(f"La casa gana la partida {i}")
            dineroJugador -= B
        elif puntosCasa > 21 or puntosJugador > puntosCasa:
            print(f"El jugador gana la partida {i}")
            dineroJugador += B
        else:
            print(f"La casa gana la partida {i}")
            dineroJugador -= B
                
    print(f"El jugador tiene {dineroJugador} pesos")
    
if __name__ == '__main__':
    main()