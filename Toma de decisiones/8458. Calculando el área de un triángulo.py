import math

def distancia(x1, y1, x2, y2, x3, y3):
    d1 = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    d2 = math.sqrt(pow(x3 - x2, 2) + pow(y3 - y2, 2))
    d3 = math.sqrt(pow(x1 - x3, 2) + pow(y1 - y3, 2))
    
    s = (d1 + d2 + d3) / 2
    
    return math.sqrt(s * (s - d1) * (s - d2) * (s - d3))


x1, y1, x2, y2, x3, y3 = map(float, input().split())
area = distancia(x1, y1, x2, y2, x3, y3)
print(f"{area: 5f}")