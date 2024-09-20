def imprimirCorazones(M):
    
    for i in range(M):
        N = int(input())
        for j in range(N):
            print("<3", end="")
            
        print()
        
def main():
    M = int(input())
    
    imprimirCorazones(M)
    
if __name__ == '__main__':
    main()