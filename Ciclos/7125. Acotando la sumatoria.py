def main():
    
    K = 1
    x = 8
    N = int(input())
    
    while (N > 0):
        N -= x
        K += 1
        x += 1
        
    print(K - 1)
    
if __name__ == '__main__':
    main()