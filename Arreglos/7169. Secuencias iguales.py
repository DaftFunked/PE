def main():
    
    N = int(input())
    
    n = list(map(int, input().split()))
    
    m = list(map(int, input().split()))
    
    igualdad = 1
    
    for i in range(N):
        if n[i] != m[i]:
            igualdad = 0
            
    print(igualdad)
    
if __name__ == '__main__':
    main()