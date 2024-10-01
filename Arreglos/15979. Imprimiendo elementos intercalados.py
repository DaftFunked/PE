def main():
    
    N = int(input())
    
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    for i in range(N):
        if i % 2 == 0:
            print(A[i], end=" ")
        else:
            print(B[i], end=" ")

if __name__ == '__main__':
    main()