def main():
    N = int(input())

    matriz1 = [[0] * N for _ in range(N)]
    matriz2 = [[0] * N for _ in range(N)]
    suma = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            matriz1[i][j] = int(input())

    for i in range(N):
        for j in range(N):
            matriz2[i][j] = int(input())

    for i in range(N):
        for j in range(N):
            suma[i][j] = matriz1[i][j] + matriz2[i][j]

    for i in range(N):
        for j in range(N):
            print(suma[i][j], end = " ")
        print()
        
if __name__ == '__main__':
    main()