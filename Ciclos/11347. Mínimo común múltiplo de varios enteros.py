def mcd(a, b):
    if (b == 0):
        return a
    else:
        return mcd(b, a % b)
    
def mcm(a, b):
    return (a * b) / mcd(a, b)

def main():
    n = int(input())
    
    N = list(map(int, input().split()))
        
    for i in range(0, n - 1):
        N[i + 1] = int(mcm(N[i], N[i + 1]))
        
    
    print(N[n-1])
        
if __name__ == "__main__":
    main()