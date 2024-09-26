def main():
    
    N = int(input())
    
    n = list(map(int, input().split()))
    
    inicio = 0
    fin = N - 1
    
    esCapicua = True
    
    while(inicio < fin):
        if (n[inicio] != n[fin]):
            esCapicua = False
            break
        
        inicio += 1
        fin -= 1
        
    if esCapicua:
        print("SI")
    else:
        print("NO")
        
if __name__ == '__main__':
    main()