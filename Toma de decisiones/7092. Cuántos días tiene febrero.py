def bisiesto(A):
    if (A % 4 == 0 and A % 100 != 0 or A % 400 == 0):
        return 29
    else:
        return 28
    
A1, A2, A3, A4 = map(int, input().split())

print(bisiesto(A1), " ", bisiesto(A2), " ", bisiesto(A3), " ", bisiesto(A4))