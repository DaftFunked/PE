import math
import itertools


def distancia(punto1, punto2):
    return math.sqrt(math.pow(punto2[0] - punto1[0], 2) + math.pow(punto2[1] - punto1[1], 2))

A = tuple(map(float, input().split()))
B = tuple(map(float, input().split()))
C = tuple(map(float, input().split()))
D = tuple(map(float, input().split()))

puntos = [A, B, C, D]
nombres = ['A', 'B', 'C', 'D']

mejor_permutacion = []
menor_distancia = float('inf')

for permutacion in itertools.permutations(range(4)):
    distancia_total = 0
    for i in range(3):
        distancia_total += distancia(puntos[permutacion[i]], puntos[permutacion[i+1]])

    if distancia_total < menor_distancia:
        menor_distancia = distancia_total
        mejor_permutacion = permutacion
        
        
        
for i in mejor_permutacion:
    print(nombres[i], end=" ")
print()    
print(f"{menor_distancia:.5f}")