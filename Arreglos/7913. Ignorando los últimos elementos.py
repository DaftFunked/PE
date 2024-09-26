def main():
    
    N = int(input())
    
    n = list(map(int, input().split()))
    
    K = int(input())
    
    for i in range(N - K):
        print(n[i], end=" ")
        
if __name__ == '__main__':
    main()