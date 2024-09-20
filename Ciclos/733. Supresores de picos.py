def main():
    
    n = int(input())
    
    for _ in range(n):
        
        datos = list(map(int, input().split()))
        k = datos[0]
        tomas = datos[1:]
        
        
        suma = sum(tomas)
        
        aparatos = suma - (k - 1)
        
        print(aparatos)
        
if __name__ == '__main__':
    main()