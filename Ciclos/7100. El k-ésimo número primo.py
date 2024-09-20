import math

def esPrimo(n):
    if (n == 1):
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
        
    return True


def calcularPrimo(K):
    contador = 0
    numero = 1
    
    while (contador < K):
        if (esPrimo(numero)):
            contador += 1
        numero += 1
        
    return numero - 1

def main():
    
    K = int(input())
    
    resultado = calcularPrimo(K)
    
    print(resultado)
    

if __name__ == '__main__':
    main()