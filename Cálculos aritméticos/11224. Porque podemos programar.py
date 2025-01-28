def main():
    
    x = float(input())
    
    y = (((x + x ** 2) / ((5 * x) + 3)) + x) * (((x + x ** 2) / ((5 * x) + 3)) / (((x + x ** 2) / ((5 * x) +3)) + 2 * x))
    
    print(y)
    
if __name__ == '__main__':
    main()