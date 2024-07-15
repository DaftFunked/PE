def hueso(L1, T1, L2, T2):
    if ((L1 > L2) and (T1 > T2)):
        return "Hueso 1"
    elif ((L2 > L1) and (T2 > T1)):
        return "Hueso 2"
    else:
        return "Perrito confundido :("
    
L1, T1 = map(int, input().split())
L2, T2 = map(int, input().split())

print(hueso(L1, T1, L2, T2))