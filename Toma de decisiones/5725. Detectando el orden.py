A, B, C = map(int, input().split())

if (A == B and A == C and B == C and C == B):
    print("I")
elif (A >= B and B >= C):
    print("D")
elif (A <= B and B <= C):
    print("C")
else:
    print("X")