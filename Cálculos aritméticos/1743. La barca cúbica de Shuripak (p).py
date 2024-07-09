L, P, N, M = map(int, input().split())

A = 6 * (pow(L, 2))

ap = (P - 1) * (pow(L, 2))
al = P * (N - 1) * (pow(L, 2) / N)
aa = P * (M - 1) * (pow(L, 2) / M)

B = ap + al + aa 

print(int(A), " ", int(B))