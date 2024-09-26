def main():
    
    N = int(input())
    n = list(map(int, input().split()))
        
    K = int(input())
    
    for i in range(K, N):
        print(n[i], end=" ")
        
if __name__ == '__main__':
    main()