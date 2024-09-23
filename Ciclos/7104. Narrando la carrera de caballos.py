def main():
    
    T = int(input())
    avances = []
    
    for _ in range(T):
        A1, A2 = map(int, input().split())
        avances.append((A1, A2))
    
    dc1 = 0
    dc2 = 0
    diferencia = 0
    posicionAnterior = "empate"
    
    for minuto in range(T):
        A1, A2 = avances[minuto]
        dc1 += A1
        dc2 += A2
        
        diferenciaActual = abs(dc1 - dc2)
        if diferenciaActual > diferencia:
            diferencia = diferenciaActual

        if dc1 > dc2:
            if posicionAnterior != "caballo 1":
                print(f"Al minuto {minuto + 1} el caballo 1 toma la delantera")
                posicionAnterior = "caballo 1"
        elif dc2 > dc1:
            if posicionAnterior != "caballo 2":
                print(f"Al minuto {minuto + 1} el caballo 2 toma la delantera")
                posicionAnterior = "caballo 2"
        elif dc1 == dc2:
            if posicionAnterior != "empate":
                print(f"Al minuto {minuto + 1} los caballos van empatados")
                posicionAnterior = "empate"
            
    if dc1 > dc2:
        print(f"Termina la carrera y gana el caballo 1")
    elif dc2 > dc1:
        print(f"Termina la carrera y gana el caballo 2")
    else:
        print(f"Termina la carrera y empatan los caballos")
        
    print(f"La distancia maxima entre los caballos fue de {diferencia}")
    
if __name__ == '__main__':
    main()