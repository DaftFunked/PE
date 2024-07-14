P1, P2, P3, P4 = map(int, input().split())

if ((P1 == P2 and P1 == P3 and P2 == P3)) or ((P1 == P2 and P1 == P4 and P2 == P4)) or ((P1 == P3 and P1 == P4 and P3 == P4)) or ((P2 == P3 and P2 == P4 and P3 == P4)):
    print("1")
else:
    print("0")
