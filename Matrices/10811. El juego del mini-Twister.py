def main():
    N = int(input())
    A = [[0] * N for _ in range(N)]
    P = [None] * (N * N)

    for i in range(N):
        fila = list(map(int, input().split()))
        for j in range(N):
            n = fila[j]
            A[i][j] = n
            P[n - 1] = (i, j)
            
    saltos = 0
    for k in range(1, N * N):
        x1, y1 = P[k - 1]
        x2, y2 = P[k]
        saltos += abs(x1 - x2) + abs(y1 - y2)

    print(saltos)
    
if __name__ == '__main__':
    main()