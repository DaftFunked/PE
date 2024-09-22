import math

def ternas(m, n):
    
    contador = 0
    
    for a in range(m, n + 1):
        for b in range(a, n + 1):
            cuadrado = (math.pow(a, 2) + math.pow(b, 2))
            c = int(math.sqrt(cuadrado))
            if math.pow(c, 2) == cuadrado and m <= c <= n:
                contador += 1
    return contador

def main():
    
    m, n = map(int, input().split())
    
    resultado = ternas(m, n)
    
    print(resultado)
    
if __name__ == '__main__':
    main()