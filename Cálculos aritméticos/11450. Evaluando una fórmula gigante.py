x, y, z = map(float, input().split())
w = ((2*x + y) / z) * (pow(y,3) - z) / (((x + 2*y + 3*z) / (z - 2*y - 3*x)) + pow(x,2) + pow(z, 2))
print(w)