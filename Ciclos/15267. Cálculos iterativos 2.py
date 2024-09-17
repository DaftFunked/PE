def main():
    
    A, B = map(int, input().split())
    
    while (A < 4000 and B < 4000):
        for i in range(1, 6):
            A += B
            B //= 2
            
        while (B < 100):
            B += 3
            
    print(A, B, end=" ")
    
if __name__ == '__main__':
    main()