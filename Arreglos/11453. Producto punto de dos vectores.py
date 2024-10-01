def main():
    
    n = int(input())
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    productoPunto = 0
    
    for i in range(n):
        productoPunto += a[i] * b[i]
        
    print(productoPunto)
    
    
if __name__ == '__main__':
    main()