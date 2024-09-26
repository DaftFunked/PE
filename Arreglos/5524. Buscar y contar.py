def main():
    
    N = int(input())
    secuencia = list(map(int, input().split()))
    
    B = int(input())
    
    contador = 0
    
    for i in range(N):
        if secuencia[i] == B:
            contador += 1
            
    print(contador)
    
if __name__ == '__main__':
    main()