def main():
    
    T, N = map(int, input().split())
    
    H = list(map(int, input().split()))
    
    for i in range(N):
        T -= H[i]
        if T <= 0:
            print (i + 1)
            return 
    print(0)

if __name__ == '__main__':
    main()