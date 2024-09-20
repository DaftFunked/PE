import math

def esPrimo(n):
    
    if (n == 1):
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            return False
        
    return True

def encontrar(m, primos):
    
    mayor = 1
    
    for i in range(len(primos) - 1, - 1, -1):
        primo = primos[i]
        if (primo <= m):
            mayor = primo
            break
        
    return mayor    

def encontrarSuma(m, primos):
    
    resultado = [0] * (m + 1)
    
    while m > 0:
        mayor = encontrar(m, primos)
        resultado[mayor] += 1
        m -= mayor
    
    return resultado

def main():
    
    m = int(input())
    
    primos = []
    
    for n in range(2, m + 1):
        if esPrimo(n):
            primos.append(n)
            
    resultado = encontrarSuma(m, primos)
    
    for i in range(len(resultado) - 1, -1, -1):
        if resultado[i] > 0:
            print(i, end=" ")
            
    print()
    
if __name__ == '__main__':
    main()