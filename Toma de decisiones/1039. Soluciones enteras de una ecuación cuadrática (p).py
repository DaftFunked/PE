import math

a, b, c = map(int, input().split())

if (a == 0):
    if (b == 0):
        if (c == 0):
            s = -1
        else:
            s = 0
    else:
        x = -c // b
        if x.is_integer():
            s = 1
        else:
            s = 0
else:
    D = math.pow(b,2) - (4 * a * c)            
    if (D < 0):
        s = 0
    elif D == 0:
        x = -b // (2 * a)
        if x.is_integer():
            s = 1
        else:
            x = 0
    else:
        x1 = (-b + math.sqrt(D)) // (2 * a)    
        x2 = (-b - math.sqrt(D)) // (2 * a)
        s = 0
        if x1.is_integer():
            s += 1
        if x2.is_integer() and x1 != x2:
            s += 1
            
print(s)