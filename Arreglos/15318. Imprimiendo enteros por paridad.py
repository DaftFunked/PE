def main():
    
    N = int(input())
    
    arreglo = list(map(int, input().split()))
    
    P = int(input())
    
    if P == 0:
        for i in range(N):
            if arreglo[i] % 2 == 0:
                print(arreglo[i], end=" ")
                
    else:
        for i in range(N):
            if arreglo[i] % 2 != 0:
                print(arreglo[i], end=" ")

if __name__ == '__main__':
    main()