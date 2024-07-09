n = int(input())

k = 20
u = 18
t = 20
b = 20

kt = k * u
kk = kt * t
kb = kk * b

B = n // kb
n %= kb

K = n // kk
n %= kk 

T = n // kt
n %= kt

u = n // k
d = n % k

print(B, " ", K, " ", T, " ", u, " ", d)