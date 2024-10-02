def main():
    
    N = int(input())
    
    arreglo = list(map(int, input().split()))
    
    actual = 0
    saltos = 0
    while actual != N - 1:
        salto = arreglo[actual]
        actual += salto
        saltos += 1
        
    print(saltos)
    
if __name__ == '__main__':
    main()