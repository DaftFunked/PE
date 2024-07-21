def dia_semana(a, m, d):
    if (m > 2):
        m -= 2
    else:
        m += 10
        a -= 1
        
    c = a // 100
    e = a % 100
    b = ((13 * m - 1) // 5) + (e // 4) + (c // 4)
    f = (b + e + d + (5 * c)) % 7
    
    return f

a, m, d = map(int, input().split())

f2 = dia_semana(a, m, d)
f1 = 6 if f2 == 0 else f2 - 1
f3 = 0 if f2 == 6 else f2 + 1

print(f"{f1} {f2} {f3}")