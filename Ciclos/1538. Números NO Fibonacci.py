def esFibonacci(n):
    
    a = 1 
    b = 1
    
    while (b < n):
        temp = b
        b = a + b
        a = temp
        
    return b == n

def main():
    
    N = int(input())
    
    for i in range(1, N):
        if not esFibonacci(i):
            print(i, end=" ")
            
    print()
    
if __name__ == '__main__':
    main()