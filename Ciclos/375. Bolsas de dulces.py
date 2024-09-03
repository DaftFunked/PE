def main():
    
    N = int(input())
    
    suma = 0
    
    for _ in range(N):
        a, b = list(map(int, input().split()))
        suma += a * b
        
    print(suma)
    
if __name__ == "__main__":
    main()