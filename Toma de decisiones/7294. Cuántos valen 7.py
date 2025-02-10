def main():
    
    n, m = map(int, input().split())
    
    contador = 0
    
    if n == 7:
        contador += 1
        if m == 7:
            contador += 1
        elif m != 7:
            contador += 0
    elif m == 7:
        contador += 1
        if n == 7:
            contador += 1
        elif n != 7:
            contador += 0
            
    print(contador)
    
if __name__ == '__main__':
    main()