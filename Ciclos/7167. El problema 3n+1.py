def main():
    
    N = int(input())
    
    pasos = 0
    maximo = N
    
    while (N != 1):
        if (N % 2 == 0):
            N //= 2
        else:
            N = 3 * N + 1
        
        pasos += 1
        
        if (N > maximo):
            maximo = N
            
            
    print(pasos, maximo, end=" ")
    
if __name__ == '__main__':
    main()