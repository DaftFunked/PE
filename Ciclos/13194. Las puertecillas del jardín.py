def main():
    
    N = int(input())
    
    puerta = list(map(int, input().split()))
    
    for i in range(N):        
        if (puerta[i] == 1):
            ojo = i
        elif (puerta[i] == 2):
            mano = i
        elif (puerta[i] == 3):
            pie = i
            
            
    S = abs(pie - mano)
    T = abs(mano - ojo)
    
    print(S, " ", T)
    
if __name__ == "__main__":
    main()