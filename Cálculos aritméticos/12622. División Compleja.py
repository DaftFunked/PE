r1, i1, r2, i2 = map(float, input().split())

r = ((r1 * r2) + (i1 * i2)) / (pow(r2, 2) + pow(i2, 2))
i = ((i1 * r2) - (r1 * i2)) / (pow(r2, 2) + pow(i2, 2))

print (r, " ", i)