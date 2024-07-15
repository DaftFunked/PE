def publicidad(a, b, c):
    if ((b - c) > a):
        return "Invertir en publicidad"
    elif ((b - c) == a):
        return "No importa"
    else:
        return "No invertir en publicidad"
        
a, b, c = map(int, input().split())

print(publicidad(a, b, c))