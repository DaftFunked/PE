C1, C2 = map(float, input().split())

total = C1 + C2

if (total >= 100):
    print("Habra descuento incial para ambos")
    if (C1 > C2):
        print("Ademas, habra descuento especial para el primer comprador")
        C1 = C1 - (C1 * 0.10) - (C1 * 0.10)
        C2 = C2 - (C2 * 0.10)
        print(f"{C1:.2f} {C2:.2f}")
    elif (C1 < C2):
        print("Ademas, habra descuento especial para el segundo comprador")
        C1 = C1 - (C1 * 0.10)
        C2 = C2 - (C2 * 0.10) - (C2 * 0.10)
        print(f"{C1:.2f} {C2:.2f}")
    else:
        C1 = C1 - (C1 * 0.10)
        C2 = C2 - (C2 * 0.10)
        print(f"{C1:.2f} {C2:.2f}")
else:
    print("No habra descuento :(")
    print(f"{C1:.2f} {C2:.2f}")

    