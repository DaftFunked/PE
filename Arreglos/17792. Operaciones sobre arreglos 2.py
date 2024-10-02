def main():
    
    N, M = map(int, input().split())
    
    A = [0] * N
    
    for _ in range(M):
        P1, P2, C = map(int, input().split())
        
        if C == 0:
            for j in range(P1, P2 + 1):
                A[j] += 1
        
        elif C == 1:
            for j in range(N):
                if j < P1 or j > P2:
                    A[j] += 1
                    
                    
    print(" ".join(map(str, A)))

if __name__ == '__main__':
    main()