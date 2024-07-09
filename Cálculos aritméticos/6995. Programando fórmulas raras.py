import math
x, y, z = map(float, input().split())
print((x + x * (y + pow(z, 2))) / ((x + math.pi) * (y + math.pi)))