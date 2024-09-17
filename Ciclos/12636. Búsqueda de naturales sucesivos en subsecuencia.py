def main():
    
    N = int(input())
    
    secuencia = list(map(int, input().split()))
    ultimoNumero = 0
    indice = 0
    
    while indice < N:
        if ((secuencia[indice] == (ultimoNumero + 1))):
            ultimoNumero = secuencia[indice]
        else:
            indice += 1
            
    print(ultimoNumero)
    
if __name__ == "__main__":
    main()