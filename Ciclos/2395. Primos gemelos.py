import math

def esPrimo(n):
    
    if (n == 1):
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
        
        
    return True


def encontrarGemelos(m):
    p = m
    
    while True:
        if esPrimo(p) and esPrimo(p + 2):
            return (p, p + 2)
        p += 1
        
def main():
    m = int(input())
    
    gemelos = encontrarGemelos(m)
    
    print(gemelos[0], gemelos[1])
    

if __name__ == '__main__':
    main()