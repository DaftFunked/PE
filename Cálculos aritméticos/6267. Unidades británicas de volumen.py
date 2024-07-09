g1, c1, p1, t1, o1 = map(int, input().split())

O = 8
T = 2
P = 2
C = 4

tO = o1 + (t1 * O) + (p1 * T * O) + (c1 * P * T * O) + (g1 * C * P * T * O)

g2 = tO // (C * P * T * O)
tO %= (C * P * T * O)

c2 = tO // (P * T * O)
tO %= (P * T * O)

p2 = tO // (T * O)
tO %= (T * O)

t2 = tO // O
o2 = tO % O

print(g2, " ", c2, " ", p2, " ", t2, " ", o2)
