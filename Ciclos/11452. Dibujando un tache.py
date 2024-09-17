def tache(n):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == i or j == n - i + 1:
                print("@", end="")
            else:
                print(" ", end="")
        print()

def main():
    n = int(input())
    tache(n)

if __name__ == "__main__":
    main()