def automatizacion(A, B):
    if ((A % 2 == 0 and B % 2 == 0) or (A % 2 != 0 and B % 2 != 0)):
        A += 5
        if (A < B):
            return A
        else:
            return B
    else:
        B -= 5
        if (A > B):
            return 2 * A
        else:
            return 2 * B
        
A, B = map(int, input().split())

print(automatizacion(A, B))