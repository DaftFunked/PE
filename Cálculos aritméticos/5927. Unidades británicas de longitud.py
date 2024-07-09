u = int(input())

I = 12
P = 3
Y = 220
F = 8

IY = I * P
IF = IY * Y
IM = IF * F

m = u // IM
u %= IM

f = u // IF
u %= IF

y = u // IY 
u %= IY

p = u // I
q = u % I

print(m, " ", f, " ", y, " ", p, " ", q)