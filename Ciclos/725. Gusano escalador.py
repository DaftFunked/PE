def main():
    
    n, u, d = map(int, input().split())
    
    m = 0
    a = 0
    
    while (a < n):
        m += 1
        a += u
        
        if (a >= n):
            break
        
        a -= d
        m += 1
        
    
    print(m)
    
if __name__ == "__main__":
    main()