def main():
    
    n, m = map(int, input().split())
    
    alturas = [0] * m
    
    for i in range(n):
        fila = list(map(int, input().split()))
            
        for j in range(m):
            if fila[j] == 1:
                alturas[j] += 1
                
    print(*alturas, end=" ")
    
if __name__ == '__main__':
    main()