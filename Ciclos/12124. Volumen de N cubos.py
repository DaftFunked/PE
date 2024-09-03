import math

def main():
    
    N = int(input())
    cubo = list(map(int, input().split()))
    volumen = [0] * N
        
    for i in range (N):
        volumen[i] = int(math.pow(cubo[i], 3))
        print(volumen[i], end=" ")
        
        
if __name__ == "__main__":
    main()