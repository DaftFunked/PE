def main():
    # Leer dimensiones de la matriz
    n, m = map(int, input().split())
    
    # Inicializar la matriz A y leer los elementos
    A = []
    for _ in range(n):
        fila = list(map(int, input().split()))
        A.append(fila)
    
    # Crear la matriz transpuesta T de m x n
    T = [[0] * n for _ in range(m)]
    
    # Realizar la transposición
    for i in range(n):
        for j in range(m):
            T[j][i] = A[i][j]
    
    # Imprimir la matriz transpuesta
    for fila in T:
        print(" ".join(map(str, fila)))

# Ejecutar la función principal
if __name__ == '__main__':
    main()
