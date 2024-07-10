F = int(input())

C = (F - 32) * 5 // 9

if C <= 36:
    E = 0
else:
    E = 1
    
print(C, " ", E)