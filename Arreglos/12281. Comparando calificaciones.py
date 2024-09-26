def main():
    
    N = int(input())
    
    calf1 = list(map(int, input().split()))
    calf2 = list(map(int, input().split()))
    
    
    peores = [min(calf1[i], calf2[i]) for i in range(N)]
    mejores = [max(calf1[i], calf2[i]) for i in range(N)]
        
    
    print(" ".join(map(str, peores)))
    print(" ".join(map(str, mejores)))
        
        
if __name__ == '__main__':
    main()