def main():
    
    N = int(input())
    
    arreglo = list(map(int, input().split()))
    
    S = int(input())
    
    derecha = 0
    izquierda = 0
    arrizq = 0
    arrder = 0
    
    for i in range(N):
        izquierda += arreglo[i]
        if izquierda >= S:
            arrizq = i + 1
            break
        
    for i in range(N - 1, -1, -1):
        derecha += arreglo[i]
        if derecha >= S:
            arrder = N - i
            break
        
    print(arrizq, arrder, end=" ")
    
if __name__ == '__main__':
    main()