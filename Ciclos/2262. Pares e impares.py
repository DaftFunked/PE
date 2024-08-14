N = int(input())
    
numeros = list(map(int, input().split()))
    
par = 0
impar = 0
    
for num in numeros:
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
    
print(par, impar)
