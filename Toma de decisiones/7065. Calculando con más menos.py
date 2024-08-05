A, B, C = map(float, input().split())

if (B == 0):
    print("indefinido")
else:
    x1 = (A / B) + C
    x2 = (A / B) - C
    if (x1 == x2):
        print(f"{x1:.7f}")
    else:
        print(f"{x1:.7f} {x2:.7f}")
