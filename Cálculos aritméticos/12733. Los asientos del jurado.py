import math

def fila1(a, b, c):
    return math.pow(a, 2) - a + ((b * c) / 10) + 1

def fila2(a, b, c):
    return 1 + ((fila1(a, b, c) - 1 + (a * b * c)) % 101)

def fila3(a, b, c):
    return 1 + ((fila1(a, b, c)) / 2) + ((fila2(a, b, c)) / 2)


a, b, c = map(int, input().split())

print(int(fila1(a, b, c)), " ", int(fila2(a, b, c)), " ", int(fila3(a, b, c)))