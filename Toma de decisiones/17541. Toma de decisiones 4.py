def automatizacion(A, B, C):
    if ((A % C == 0 and B % C == 0)):
        A -= 10
        if (A > C):
            return 2 * A
        else:
            return A + C
    else:
        B += 5
        if (C < B):
            return C
        else:
            return B
        
        
A, B, C = map(int, input().split())

print(automatizacion(A, B, C))