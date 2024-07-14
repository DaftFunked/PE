import math

Xa, Ya, Xb, Yb = map(int, input().split())

distancia = math.sqrt(math.pow((Xa - Xb), 2) + math.pow((Ya - Yb), 2))

if (distancia >= 150):
    print("sana")
else:
    print("insana")