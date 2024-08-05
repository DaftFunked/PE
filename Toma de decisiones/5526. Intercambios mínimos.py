def intercambio(A, B, C):
    intercambios = 0
    if (C < A):
        A, C = C, A
        intercambios += 1
    
    if (C < B):
        B, C = C, B
        intercambios += 1
        
    if (B < A):
        B, A = A, B
        intercambios += 1
        
    return intercambios

A, B, C = map(int, input().split())
resultado = intercambio(A, B, C)

print(resultado)