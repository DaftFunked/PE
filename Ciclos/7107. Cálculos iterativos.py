def main():
    
    N = 0
    
    A, B, C = map(int, input().split())
    
    for i in range(1, A + 1):
        if i % 2 != 0:
            N += i
    
    potencia = 1
    while potencia <= B:
        N -= potencia
        potencia *= 2
        
    while N % C == 0 and N != 0:
        N //= C
        
    print(N)
    
if __name__ == '__main__':
    main()