import math

def contraTriangulos(m, n):
    contador = 0
    
    for a in range(m, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a + b > c and a + c > b and b + c > a:
                    if math.pow(a, 2) + math.pow(b, 2) > math.pow(c, 2) and math.pow(b, 2) + math.pow(c, 2) > math.pow(a, 2) and math.pow(c, 2) + math.pow(a, 2) > math.pow(b, 2):
                        contador += 1
                        
    return contador

def main():
    
    m, n = map(int, input().split())
    
    resultado = contraTriangulos(m, n)
    
    print(resultado)
    
if __name__ == '__main__':
    main()