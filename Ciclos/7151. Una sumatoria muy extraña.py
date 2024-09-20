def main():
    
    a, b = map(int, input().split())
    
    m = 0
    n = 0
    
    suma = 0
    
    for i in range(1, a + 1):
        m += i
    
    for j in range(1, b + 1):
        n += j
        
    for i in range(m, n + 1):
        suma += i
        
        
    print(suma)
    
if __name__ == '__main__':
    main()