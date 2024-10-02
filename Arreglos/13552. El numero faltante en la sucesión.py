def main():
    
    n = int(input())
    
    numeros = []
    
    while len(numeros) < n - 1:
        numeros.extend(map(int, input().split()))
    
    suma = n * (n + 1) // 2
    actual = sum(numeros)
    
    faltante = suma - actual
    
    print(faltante)
    
    
if __name__ == '__main__':
    main()