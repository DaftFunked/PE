def main():
    
    N = int(input())
    
    mermelada = [[0 for _ in range(2)] for _ in range(N)]
    
    for i in range(N):
        mermelada[i][0], mermelada[i][1] = map(int, input().split())
        
    dp = [[0 for _ in range(2)] for _ in range(N)]
    dp[0][0] = mermelada[0][0]
    dp[0][1] = mermelada[0][1]
    
    for i in range(1, N):
        dp[i][0] = mermelada[i][0] + max(dp[i - 1][0], dp[i - 1][1])
        dp[i][1] = mermelada[i][1] + max(dp[i - 1][0], dp[i - 1][1])
        
    maxMermelada = max(dp[N - 1][0], dp[N - 1][1])
    
    print(maxMermelada)
    
if __name__ == "__main__":
    main()