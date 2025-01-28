def main():
    
    N, M = map(int, input().split())
    
    restantes = (N - (N // 2)) % M
    
    print(int(restantes))
    
if __name__ == '__main__':
    main()