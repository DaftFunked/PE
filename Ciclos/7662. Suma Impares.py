a, b = map(int, input().split())

if (a % 2 == 0):
    a += 1
if (b % 2 == 0):
    b -= 1
    
suma = 0

for i in range(a, b + 1, 2):
    suma += i
    
print(suma)