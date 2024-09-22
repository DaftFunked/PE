def main():
    
    n, k = map(int, input().split())
    
    hojas = list(map(int, input().split()))
    
    cuadernos = 0
    usadas = 0
    
    for i in range(n):
        if usadas + hojas[i] > k:
            cuadernos += 1
            usadas = hojas[i]
        else:
            usadas += hojas[i]
            
    if usadas > 0:
        cuadernos += 1
        
    print(cuadernos)
    
if __name__ == '__main__':
    main()