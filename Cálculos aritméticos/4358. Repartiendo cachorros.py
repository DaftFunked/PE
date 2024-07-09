C, P, H = map(int, input().split())

S = (C - P) % (H + 1)

print(P + S)