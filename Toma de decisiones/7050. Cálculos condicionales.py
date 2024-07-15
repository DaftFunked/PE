def calculos(N):
    modificado = 0
    if (N % 2 == 0):
        N //= 2
        modificado += 1
    else:
        N += 1
        modificado += 1
        
    if (N >= 100):
        N //= 100
        modificado += 1
    elif (N >= 10):
        N //= 10
        modificado += 1
        
    if ( N % 3 == 0):
        N -= 1
        modificado += 1
        
    return N, modificado

N = int(input())
r = calculos(N)

print(r[0], r[1])