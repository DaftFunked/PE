def main():
    # Leer N y M en una sola línea
    N, M = map(int, input().split())

    matriz1 = []
    matriz2 = []

    # Leer la primera matriz y verificar el tamaño de cada fila
    for i in range(N):
        fila = list(map(int, input().split()))
        if len(fila) != M:
            return  # Termina el programa si el tamaño es incorrecto
        matriz1.append(fila)

    print()
    
    # Leer la segunda matriz y verificar el tamaño de cada fila
    for _ in range(N):
        while True:    
            fila = input().strip()
            if fila:
                matriz2.append(list(map(int, fila.split())))
                break

    # Calcular la matriz de suma
    suma = []
    for i in range(N):
        filaSuma = []
        for j in range(M):
            filaSuma.append(matriz1[i][j] + matriz2[i][j])
        suma.append(filaSuma)
    
    print()
    # Imprimir la matriz resultante
    for fila in suma:
        print(' '.join(map(str, fila)))
        
if __name__ == '__main__':
    main()