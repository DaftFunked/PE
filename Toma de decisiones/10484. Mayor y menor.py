A, B, C, D, E = map(int, input().split())

if A >= B and A >= C and A >= D and A >= E:
    Q = A
elif B >= A and B >= C and B >= D and B >= E:
    Q = B
elif C >= A and C >= B and C >= D and C >= E:
    Q = C
elif D >= A and D >= B and D >= C and D >= E:
    Q = D
else:
    Q = E

if A <= B and A <= C and A <= D and A <= E:
        P = A
elif B <= A and B <= C and B <= D and B <= E:
        P = B
elif C <= A and C <= B and C <= D and C <= E:
        P = C
elif D <= A and D <= B and D <= C and D <= E:
        P = D
else:
        P = E

print(P, " ", Q)