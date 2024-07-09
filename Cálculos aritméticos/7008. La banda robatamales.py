T, B = map(int, input().split())

L = (T // 2) + (T % 2)
R = T - L
S = R % (B - 1)
print(L+S)