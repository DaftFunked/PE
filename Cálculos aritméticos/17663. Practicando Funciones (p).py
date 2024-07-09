import math

def h(x, y, z):
    return f(x // y) + 3 * g(z // y, x)

def g(b, c):
    return (7 * b - 3) % (c * c + 1)

def f(a):
    return (4 * (a ** 3)) + g(2 * a, -3 * a)

x, y, z = map(int, input().split())
print(int(h(x, y, z)))