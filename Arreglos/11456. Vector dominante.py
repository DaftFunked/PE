def main():
    
    n = int(input())
    
    secuencia1 = list(map(int, input().split()))
    secuencia2 = list(map(int, input().split()))
    
    propiedad = True
    
    for i in range(n):
        if secuencia1[i] <= secuencia2[i]:
            propiedad = False
            break
        
        
    if propiedad:
        print("1")
    else:
        print("0")
        
        
if __name__ == '__main__':
    main()