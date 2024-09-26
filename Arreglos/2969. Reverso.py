def main():
    
    N = int(input())
    
    n = list(map(int, input().split()))
    
    for i in range(N - 1, -1, -1):
        print(n[i], end=" ")
        
if __name__ == '__main__':
    main()