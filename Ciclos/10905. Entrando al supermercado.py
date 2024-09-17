def main():
    # Read N and M
    N, M = map(int, input().split())
    
    inicio = 0
    
    for i in range(N):  
        C = int(input()) 
        if (inicio + C) < M or (inicio + C) == M:
            inicio += C
            print("\tpasa")
        else:
            print("\tespera")

if __name__ == "__main__":
    main()
