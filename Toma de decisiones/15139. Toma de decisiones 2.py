def automatizacion(A, B):
    if (A % 2 == 0 or B % 2 == 0):
        A += 5
        if (A >= B):
            return A + B
        else:
            return A - B
    else:
        B -= 5
        return A * B
    
A, B = map(int, input().split())

print(automatizacion(A, B))