E1, E2, E3 = map(float, input().split())
T1, T2, T3 = map(float, input().split())

E = ((E1 + E2 + E3) / 3)
T = ((T1 + T2 + T3) / 3)
P = (E * 0.4) + (T * 0.6)

if (P >= 6.0 and E >= 6.0):
    print("aprobado", P)
elif (P >= 6.0 and E < 6.0):
    print("reprobado")
else:
    print("reprobado")