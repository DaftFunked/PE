def main():
    V = int(input())
    
    d = sum(map(int, input().split()))
    
    A = d // 365
    
    print(A)
    
if __name__ == "__main__":
    main()