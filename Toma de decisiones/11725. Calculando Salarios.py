def calcHoras(h):
    t = int(0)
    if (h <= 40):
        return h
    elif (h <= 48):
        t = h % 40
        return (t * 2) + calcHoras(h - t)
    else:
        t = h % 48
        return (t * 3) + calcHoras(h - t)
    
s, h = map(int, input().split())

print(calcHoras(h) * s)
        