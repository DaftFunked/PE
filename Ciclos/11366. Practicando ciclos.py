def main():
    
    N, A, B = map(int, input().split())
    
    while (N < 1000):
        if (N % 2 == 0):
            for i in range(1, A + 1):
                N += i
        else:
            for i in range(1, B + 1):
                N += i
                
    print(N)
    
if __name__ == "__main__":
    main()