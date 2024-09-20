def factorial(x):
    resultado = 1
    for i in range(1, x + 1):
        resultado *= i
    return resultado

def permutaciones(n, r):
    return factorial(n) // factorial(n - r)

def contar(a, b, c, d):
    numeros = b - a + 1
    num = permutaciones(numeros, 3)
    
    letras = d - c + 1
    let = permutaciones(letras, 2)
    
    placas = num * let
    
    return placas

def main():
    
    a, b, c, d = list(map(int, input().split()))
    
    res = contar(a, b, c, d)
    
    print(res)
    
if __name__ == '__main__':
    main()