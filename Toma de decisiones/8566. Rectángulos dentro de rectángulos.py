def rectangulo(A, B, C, D):
    S = 0
    G = 0
    
    if ((A <= C and B <= D)):
        S = 1
    elif ((C <= A and D <= B)):
        S = 2
    else:
        if (A <= D and B <= C):
            S = 1
            G = 1
        elif (C <= B and D <= A):
            S = 2
            G = 1
            
    print(S, G)

A, B, C, D = map(int, input().split())

rectangulo(A, B, C, D)