import math


def main():
    N = int(input())
    
    suma = 0
    
    for i in range (0, int(math.log2(N)) + 1):
        termino = N // int(math.pow(2, i))
        suma += termino
        
    print(suma)
        
if __name__ == "__main__":
    main()