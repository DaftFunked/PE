def dibujarRectangulo(N, M):
    for i in range(N):
        for j in range(M):
            print("*", end="")
        print()

def main():
    
    N, M = map(int, input().split())
    
    dibujarRectangulo(N, M)
    
if __name__ == '__main__':
    main()