def main():
    
    n, a, b, c = map(int, input().split())
    
    total = 0
    
    for i in range(1, n + 1):
        if i % a == 0:
            total += i
            
    for i in range(1, n + 1):
        if i % b == 0:
            total += i
            
    for i in range(1, n + 1):
        if i % c == 0:
            total += i
            
    print(total)
    
if __name__ == "__main__":
    main()
