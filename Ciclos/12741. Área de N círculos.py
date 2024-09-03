import math

def main():
    
    pi = 3.1416
    N = int(input())
    
    radio = list(map(float, input().split()))
    
    area = [0] * N
    
    for i in range(N):
        area[i] = pi * (radio[i]**2)
        print(f"{area[i]:.6f}", end=" ")
        
if __name__ == "__main__":
    main()