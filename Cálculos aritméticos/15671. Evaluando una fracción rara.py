x, y, z = map(float, input().split())

w = (pow(x, 1.2 * y) - z + 5.7) / ((x + (2 * y) + (3 * z)) / (x * y))

print(w)