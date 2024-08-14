def sumaDigitos(n):
    suma = 0
    while n > 0:
        ultimo = n % 10
        suma += ultimo
        n //= 10
    return suma

n = int(input())

resultado = sumaDigitos(n)

print(resultado)