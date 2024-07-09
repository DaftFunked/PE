N, M = map(int, input().split())

T = N // 2
R = N - T
A = R // M
S = R % M

print(S)