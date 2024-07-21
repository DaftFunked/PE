def bisiesto(A):
    if ((A % 4 == 0) and (A % 100 != 0) or (A % 400 == 0)):
        return 1
    else:
        return 0
    
A1, A2, A3, A4, A5, A6, A7, A8, A9, A10 = map(int, input().split())

total = (bisiesto(A1) + bisiesto(A2) + bisiesto(A3) + bisiesto(A4) + bisiesto(A5) + bisiesto(A6) + bisiesto(A7) + bisiesto(A8) + bisiesto(A9) + bisiesto(A10))

print(total)