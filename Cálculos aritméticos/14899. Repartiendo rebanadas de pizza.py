N, A, H, M = map(int, input().split())

rh = N // 2
rm = N // 2

trh = 1
trm = 1

rh -= 1
rm -= 1

th = A + H  
tm = A + M

rah = rh // th
rrh = rh % th
trh += rrh

ram = rm // tm
rrm = rm % tm
trm += rrm

T = trh + trm

print(T)