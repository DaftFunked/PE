def main():
    
    n, m, o = map(int, input().split())
    
    A = []
    B = []
    R = [[0] * o for _ in range(n)]
    
    for _ in range(n):
        fila = list(map(int, input().split()))
        A.append(fila)
            
    for _ in range(m):
        fila = list(map(int, input().split()))
        B.append(fila)
            
    for i in range(n):
        for j in range(o):
            for k in range(m):
                R[i][j] += A[i][k] * B[k][j]
    
    print()
    for fila in R:
        print(" ".join(map(str, fila)))
        
if __name__ == '__main__':
    main()