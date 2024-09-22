def main():
    
    m, n = map(int, input().split())
    
    contador = 0
    
    for a in range(m, n + 1):
        for b in range(a, n + 1):
            for c in range(b, n + 1):
                if a + b > c and a + c > b and b + c > a:
                    contador += 1

    print(contador)
    
if __name__ == '__main__':
    main()