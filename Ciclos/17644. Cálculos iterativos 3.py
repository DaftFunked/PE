def main():
    
    A, B = map(int, input().split())
    
    while (A > 100 or B > 100):
        while (A % 2 != 0 or A > 250):
            A //= 2
        
        for i in range(1, 16):
            B -= A
            A += 3
            
            
    print(A, B, end=" ")
    
if __name__ == '__main__':
    main()