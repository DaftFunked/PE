def main():
    
    N = int(input())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    C = []

    
    for i in range(N):
        C.append(A[i])
        C.append(B[i])
        
    D = []
    
    for i in range(N - 1, -1, -1):
        D.append(A[i])
        D.append(B[i])
        
    print(*C)
    
    print(*D)
    
if __name__ == '__main__':
    main()