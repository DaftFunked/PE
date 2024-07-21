def cofre(A, B, C, X, Y, Z):
    if ((A <= X and B <= Y and C <= Z) or
        (A <= X and B <= Z and C <= Y) or
        (A <= Y and B <= X and C <= Z) or
        (A <= Y and B <= Z and C <= X) or
        (A <= Z and B <= X and C <= Y) or
        (A <= Z and B <= Y and C <= X)):
        return 1
    else:
        return 0
    
A, B, C, X, Y, Z = map(int, input().split())

print(cofre(A, B, C, X, Y, Z))