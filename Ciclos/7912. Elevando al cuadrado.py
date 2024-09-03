import math

def main():
    
    N = int(input())
    
    contador = 0
    
    while N < 30000:
        contador += 1
        N = int(math.pow(N,2))
        
    print(N, " ", contador)
    
if __name__ == "__main__":
    main()