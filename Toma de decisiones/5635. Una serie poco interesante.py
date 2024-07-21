N, P = map(int, input().split())

antes = ((N - P - 1) % 3) + 1
if (antes <= 0):
    antes += 3

despues = ((N + P - 1) % 3) + 1
if (despues == 0):
    despues = 3
    
print(antes, " ", despues)