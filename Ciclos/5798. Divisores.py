N = int(input())

D = 0

for i in range(1, N + 1):
    if (N % i == 0):
        D += 1
        
print(D)