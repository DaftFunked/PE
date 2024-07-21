def rotacion(A1, B1, C1, A2, B2, C2):
    if((A1 == A2 and B1 == B2 and C1 == C2) or
       (A1 == A2 and B1 == C2 and C1 == B2) or
       (A1 == B2 and B1 == A2 and C1 == C2) or
       (A1 == B2 and B1 == C2 and C1 == A2) or
       (A1 == C2 and B1 == A2 and C1 == B2) or
       (A1 == C2 and B1 == B2 and C1 == A2)):
        return 1
    else:
        return 0
    
A1, B1, C1 = map(int, input().split())
A2, B2, C2 = map(int, input().split())
print(rotacion(A1, B1, C1, A2, B2, C2))
       