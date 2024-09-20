def main():
    N, K, D = map(int, input().split())
    p = list(map(int, input().split()))
    p.append(K)
    
    descansos = 0
    actual = 0
    
    i = 0
    while i < len(p):
        
        siguiente = actual
        while i < len(p) and p[i] - actual <= D:
            siguiente = p[i]
            i += 1
        
        if siguiente == actual:
            break
        
        if siguiente < K:
            descansos += 1
        
        actual = siguiente
    
    print(descansos)

if __name__ == '__main__':
    main()
