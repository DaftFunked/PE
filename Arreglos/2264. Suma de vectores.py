def main():
    
    N = int(input())
    
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    
    suma = []
    
    for i in range(N):
        suma.append(num1[i] + num2[i])
        
    for i in range(N):
        print(suma[i], end = " ")
        
if __name__ == '__main__':
    main()