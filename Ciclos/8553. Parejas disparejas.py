def s(n):
    suma = 0
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            suma += i
    return suma

def pareja(a, b):
    suma = s(a)
    sumb = s(b)
    
    if suma == b and sumb == a:
        return 0
    elif suma <= b and sumb <= a:
        return 1
    elif suma >= b and sumb >= a:
        return 2
    else:
        return 3
    
def main():
    x, y = map(int, input().split())
    
    p = pareja(x, y)
    q = pareja(x, x)
    r = pareja(y, y)
    
    print(p, " ", q, " ", r)
    

if __name__ == "__main__":
    main()