import math

def main():
    
    N = int(input())
    
    A = list(map(int, input().split()))
    
    mejorDiferencia = math.inf
    mejor = 0
    izquierda = 0
    derecha = 0
    
    for K in range(1, (N // 2) + 1):
        izquierda = sum(A[:K])
        derecha = sum(A[N - K:])
        
        diferencia = abs(izquierda - derecha)
        
        if diferencia < mejorDiferencia:
            mejorDiferencia = diferencia
            mejor = K
            mejorIzquierda = izquierda
            mejorDerecha = derecha
        elif diferencia == mejorDiferencia and K < mejor:
            mejor = K
            mejorIzquierda = izquierda
            mejorDerecha = derecha
            
    print(mejor)
    print(mejorIzquierda, mejorDerecha, end=" ")
    
if __name__ == '__main__':
    main()