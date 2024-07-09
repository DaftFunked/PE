x, y = map(float, input().split())
z = (((pow(x,3) + pow(x,2)) / (pow(y,2) - y)) - ((x/y) + 5)) / (2*x)

print(z)