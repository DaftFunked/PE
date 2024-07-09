a1, b1, c1 = map(float, input().split())
a2, b2, c2 = map(float, input().split())

y = (c2 - a2 * c1 / a1) / (b2 - a2 * b1 / a1)
x = (c1 - b1 * y) / a1

print(round(x, 6), " ", round(y, 6))