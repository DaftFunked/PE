import math


n = int(input())

e = 2.71828182845904525356

for i in range (1, n + 1):
    resultado = math.pow(e, 2 * i) - i
    print(f"{i} {resultado:.3f}")
    