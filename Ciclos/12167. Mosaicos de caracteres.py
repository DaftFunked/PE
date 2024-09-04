def main():
    
    N = int(input())
    
    for fila in range(1, 3):
        for i in range(N):
            if fila == 1:
                if i % 2 != 0:
                    print("#", end="")
                else:
                    print("-", end="")
            else:
                if i % 2 != 0:
                    print("-", end="")
                else:
                    print("#", end="")
                    
        print()
if __name__ == "__main__":
    main()