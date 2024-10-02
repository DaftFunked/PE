def main():
    
    N = int(input())
    
    secuencia = list(map(int, input().split()))
    
    maximo = 0
    
    for i in range(N):
        if secuencia[i] > maximo:
            maximo = secuencia[i]
            
    lista = []
    
    for i in range(N):
        if secuencia[i] != maximo:
            lista.append(secuencia[i])
            
    M = len(lista)
    
    print(M)
    for numero in lista:
        print(numero, end = " ")
        
if __name__ == '__main__':
    main()