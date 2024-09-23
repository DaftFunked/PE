def main():
    
    N, K = map(int, input().split())
    
    alturas = list(map(int, input().split()))
    
    posible = True
    alturaMinima = 0
    
    for i in range(N - 1):
        diferencia = alturas[i + 1] - alturas[i]
        if diferencia > K:
            posible = False
            alturaMinima = max(alturaMinima, diferencia)
            
            
    if posible:
        print("POSIBLE")
    else:
        print("IMPOSIBLE", alturaMinima, end=" ")
        
if __name__ == '__main__':
    main()