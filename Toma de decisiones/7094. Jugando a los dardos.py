import math

def calcularPuntaje(x, y, a, b, c, d, e):
    distancia = math.sqrt(math.pow(x, 2) + math.pow(y,2))
    if (distancia <= a):
        return 10
    elif (distancia <= b):
        return 8
    elif (distancia <= c):
        return 6
    elif (distancia <= d):
        return 4
    elif (distancia <= e):
        return 2
    else:
        return 0
    
p, q, r, s, t, u, a, b, c, d, e = map(float, input().split())

puntajeTotal = 0
puntajeTotal += calcularPuntaje(p, q, a, b, c, d, e)
puntajeTotal += calcularPuntaje(r, s, a, b, c, d, e)
puntajeTotal += calcularPuntaje(t, u, a, b, c, d, e)

print(puntajeTotal)