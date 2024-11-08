def main():

    N = (int(input()))

    A = []

    for i in range(N):
        fila = list(map(int, input().split()))
        A.append(fila)
        
    a = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            a[j][N - 1 - i] = A[i][j]
            
    print()
    for fila in a:
        print(" ".join(map(str, fila)))
        
if __name__ == '__main__':
    main()