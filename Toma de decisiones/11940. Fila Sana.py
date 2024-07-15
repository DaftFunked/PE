def fila(P, L, S):
    if ((P - 1) * S <= L):
        return "CABEN"
    else:
        return "RIESGO"
        
P, L, S = map(int, input().split())

print(fila(P, L, S))