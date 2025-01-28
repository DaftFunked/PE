def main():
    
    x, y = map(float, input().split())
    
    z = (((x ** 3 + x ** 2) / (y ** 2 - y)) - ((x / y) + 5)) / (2 * x)
    
    print(z)
    
if __name__ == '__main__':
    main()