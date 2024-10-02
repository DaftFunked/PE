def incrementar(A, N, P):
    if P % 2 == 0:
        for i in range(N):
            if i % 2 == 0:
                A[i] += 1
    else:
        for i in range(N):
            if i % 2 != 0:
                A[i] += 1
                
                
    for i in range(N):
        if P % 2 == 0 and A[i] % 2 == 0 or P % 2 != 0 and A[i] % 2 != 0:
            A[i] += 1
            
            
def main():
    
    N = int(input())
    
    A = list(map(int, input().split()))
    
    P = int(input())
    
    incrementar(A, N, P)
    
    for i in range(N):
        print(A[i], end = " ")
        
    print()
    
    for i in range(N - 1, -1, -1):
        print(A[i], end = " ")
        
        
if __name__ == '__main__':
    main()