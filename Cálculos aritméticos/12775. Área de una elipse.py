import math

xc, yc = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

r1 = math.sqrt((pow(xc - x1, 2)) + (pow(yc - y1, 2)))
r2 = math.sqrt((pow(xc - x2, 2)) + (pow(yc - y2, 2)))

a = math.pi * r1 * r2

print(round(a,2))