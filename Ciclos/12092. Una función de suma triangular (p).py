def f (n):
    if (n == 1):
        return 1
    else:
        return (n * (n + 1)) // 2 + f(n - 1)
    
    
def main():
    
    n = int(input())
    
    if 1 <= n <= 6:
        resultado = f(f(f(n)))
        print(resultado)
    
if __name__ == "__main__":
    main()