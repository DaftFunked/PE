def automatizacion(A, B):
    C = A + B
    if (C != 5):
        A -= 1
        par = (7 * A) + B
        if (par % 2 == 0):
            return A - B
        else:
            return A * B
    else:
        B += 3
        return (2 * A) + B
    
A, B = map(int, input().split())

print(automatizacion(A, B))