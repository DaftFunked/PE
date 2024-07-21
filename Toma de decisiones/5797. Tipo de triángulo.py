def triangulo(a, b, c):
    if (a + b <= c or b + c <= a or c + a <= b):
        t = 0
        d = max(c - (a + b) + 1, max(a - (b + c) + 1, b - (c + a) + 1))
    elif (a == b and b == c):
        t = 1
        d = 0
    elif (a == b or b == c or c == a):
        t = 2
        d = 0
    else:
        t = 3
        d = 0
        
    return (t, d)

a, b, c = map(int, input().split())
t, d = triangulo(a, b, c)

print(t, " ", d)
