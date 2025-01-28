def main():
    
    a = float(input())
    
    x = (3 * a) + 15
    y = (x + 3) / (x + 1)
    z = ((5 * x) + (7 * y)) / (a * x * y)
    
    print (z)
    
if __name__ == '__main__':
    main()