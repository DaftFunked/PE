def main():
    
    N = int(input())
    
    arreglo = list(map(int, input().split()))
    
    for i in range(N // 2):
        print(arreglo[i] + arreglo[N-1-i], end=" ")
        
if __name__ == '__main__':
    main()