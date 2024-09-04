def main():
    
    N, A, B = map(int, input().split())
    
    while N < 100:
        for i in range(1, N + 1):
            print(i, end=" ")
        for i in range(N, 0, -1):
            print(i, end=" ")
        T = A * N
        
        while N < T:
            N += B
            
    
    print()
    
if __name__ == "__main__":
    main()