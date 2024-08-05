import math

A = int(input())
B = int(input())
C = int(input())

D = math.pow(B, 2) - (4 * A * C)

if (D > 0):
    x1 = (-B + math.sqrt(D)) / (2 * A)
    x2 = (-B - math.sqrt(D)) / (2 * A)
    print(min(x1, x2))
    print(max(x1, x2))
    
elif (D == 0):
    x = -B / (2 * A)
    print(x)
    
else:
    print("NA")