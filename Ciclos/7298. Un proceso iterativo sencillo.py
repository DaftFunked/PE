N = int(input())

while N < 100:
    if N % 2 == 0:
        N += 3
    else:
        N *= 2
        
print(N)