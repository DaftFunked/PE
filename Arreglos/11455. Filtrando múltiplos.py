def main():
    
    N = int(input())
    secuencia = list(map(int, input().split()))
        
    k = int(input())
    
    for i in range(N):
        if secuencia[i] % k != 0:
            print("X", end=" ")
        else:
            print(secuencia[i], end=" ")
            
if __name__ == '__main__':
    main()