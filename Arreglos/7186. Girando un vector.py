def main():
    
    N, G = map(int, input().split())
    
    X = list(map(int, input().split()))
    
    G %= N
    
    index = 0
    Y = [0] * N
    
    for i in range(N):
        index = (i + G) % N
        Y[index] = X[i]
        
    print(" ".join(map(str, Y)))
    
if __name__ == '__main__':
    main()