def main():
    p, s, r = map(int, input().split())
    
    a = 0
    d = 0
    while a < p:
        d += 1
        a += s
        if a >= p:
            break
        a -= r
    
    print(d)
    
if __name__ == "__main__":
    main()