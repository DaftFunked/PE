N = int(input())

divisores = 0


for i in range(1, N + 1):
    if (N % i == 0):
        divisores += 1
        
print(divisores)