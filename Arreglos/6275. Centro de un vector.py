def main():
    
    n = int(input())
    
    x = list(map(int, input().split()))
    
    for c in range(n + 1):
        izquierda = 0
        derecha = 0
    
        for i in range(c):
            izquierda += (c - i) * x[i]
        
        for i in range(c + 1, n + 1):
            derecha += (i - c) * x[i]
        
        if izquierda == derecha:
            print(c, izquierda)
            return
            
    print(-1, 0)
    
if __name__ == '__main__':
    main()