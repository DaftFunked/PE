def main():
    
    x = float(input())
    
    y = (x + 5) / (2 * (x + 1))
    z = (y ** 2 + x * (x - 2 * y)) / (x * y)
    
    print (z)
    
if __name__ == '__main__':
    main()