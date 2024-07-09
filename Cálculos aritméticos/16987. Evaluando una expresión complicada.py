x, y, z = map(float, input().split())

w = (pow((2 * y) + z, 2.8) - z) / ((x + y) - (x / z))

print(w)