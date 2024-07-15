def pascua(A):
    D = 0
    M = 0
    if (A >= 1583):
        B = A // 100 + 1
        C = 3 * B // 4 - 12
        E = (A % 19) + 1
        F = (8 * B + 5) // 25 - (5 + C)
        G = 5 * A // 4 - (C + 10)
        H = (11 * E + 20 + F) % 30
        if (H == 25):
            if (E > 11):
                H += 1
        elif (H == 24):
            H += 1
            
        I = 44 - H 
        if (I < 21):
            I += 30
        J = I + 7 - ((G + I) % 7)
        if (J <= 31):
            M = 3
            D = J
        else:
            M = 4
            D = J - 31
    return (D, M)

A = int(input())
D, M = pascua(A)

print(D, " ", M)