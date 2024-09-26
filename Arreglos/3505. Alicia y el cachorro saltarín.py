def main():
    
    N = int(input())
    saltosCachorro = list(map(int, input().split()))
    
    A = int(input())
    
    caidas = 0
    posicion = 0
    
    for salto in saltosCachorro:
        posicion += salto
        if posicion == A:
            caidas += 1
            
    print(caidas)
    
if __name__ == '__main__':
    main()