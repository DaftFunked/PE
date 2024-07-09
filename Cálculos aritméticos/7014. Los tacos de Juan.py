N, O, P, C = map(int, input().split())

canasta = N // C
N %= C
platon = N // P
N %= P
orden = N // O
N %= O

T = canasta * 1500 + platon * 250 + orden * 50 + N * 10

print(int(T))
print(int(N), " ", int(orden), " ", int(platon), " ", int(canasta))