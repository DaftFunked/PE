import math

def esPrimo(n):
    
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def primos(n):
    
    listaPrimos = []
    for i in range(2, n + 1):
        if esPrimo(i):
            listaPrimos.append(i)
            
    return listaPrimos

def sumaPrimos(n, listaPrimos, setPrimos):
    
    for p in listaPrimos:
        if p > n:
            break
        q = n - p
        if q in setPrimos:
            return p, (n - p)
    
    return 0, 0

def main():
    
    n = int(input())
    listaPrimos = primos(n)
    setPrimos = set(listaPrimos)
    
    if esPrimo(n):
        print(n, 0)
    else:
        p, q = sumaPrimos(n, listaPrimos, setPrimos)
        
        if p > 0:
            if p >= q:
                print(p, q)
            else:
                print(q, p)
        else:
            print(0, 0)
            
if __name__ == '__main__':
    main()