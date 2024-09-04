def main():
    
    N = int(input())
    
    numeros = list(map(int, input().split()))
    
    mayor = numeros[0]
    
    for i in range(N):        
        if numeros[i] > mayor:
            mayor = numeros[i]
            
            
    print(mayor)
    

if __name__ == "__main__":
    main()