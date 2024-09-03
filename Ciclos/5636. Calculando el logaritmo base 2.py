import math

def main():
    
    N = int(input())
    
    logaritmo = 0
    
    for i in range (2, N + 1):
        logaritmo = int(math.log2(N))
        break
    
    print(logaritmo)
    
if __name__ == "__main__":
    main()