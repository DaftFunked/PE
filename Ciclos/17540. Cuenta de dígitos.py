N = int(input())

digitos = 0

if (N == 0):
    digitos = 1
else:
    while(N > 0):
        N //= 10
        digitos += 1
        
        
print(digitos)