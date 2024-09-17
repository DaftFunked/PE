import math

def main():
    
    N = int(input())
    
    X = [] 
    Y = []
    
    longitud = 0
    
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
        
    for i in range(N - 1):
        distancia = math.sqrt((X[i+1] - X[i])**2 + (Y[i+1] - Y[i])**2)
        longitud += distancia
        
    
    suma = math.sqrt((X[N - 1] - X[0])**2 + (Y[N - 1] - Y[0])**2)
    longitud += suma
    
    print(f"{longitud:.2f}")

if __name__ == "__main__":
    main()