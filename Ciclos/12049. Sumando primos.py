import math

def esPrimo(n):
    if (n == 1):
        return False
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if (n % divisor == 0):
            return False
        
        
    return True

def main():
    n = int(input())

    t = 0
    s = 0
    numero = 1

    for numero in range(1, n + 1):
        if (esPrimo(numero) == True):
            t += 1
            s += numero
            
    print(t, " ", s)

if __name__ == "__main__":
    main()