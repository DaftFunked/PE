def intervalo(a1, a2, b1, b2):
    if (a2 >= b1 and b2 >= a1):
        return 1
    else:
        return 0
    
a1, a2, b1, b2 = map(int, input().split())

print(intervalo(a1, a2, b1, b2))