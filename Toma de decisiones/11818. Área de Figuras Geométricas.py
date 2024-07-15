import math

n = int(input())

if (n == 0):
    BM, BN, H = map(float, input().split())
    A = ((BM + BN) * H) / 2
    print("Trapecio")
    print(f"{A:.3f}")
elif (n == 1):
    B, H = map(float, input().split())
    A = (B * H) / 2
    print("Triangulo")
    print(f"{A:.3f}")
elif (n == 2):
    L = float(input())
    A = math.pow(L, 2)
    print("Cuadrado")
    print(f"{A:.3f}")
elif (n == 3):
    B, H = map(float, input().split())
    A = B * H
    print("Rectangulo")
    print(f"{A:.3f}")
elif (n == 4):
    R = float(input())
    A = (math.pi) * (math.pow(R, 2))
    print("Circulo")
    print(f"{A:.3f}")
else:
    print("Figura no vlaida")