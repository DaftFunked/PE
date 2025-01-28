def main():
    
    a, b, c = map(int, input().split())
    
    print (a + b, a + c, b + c, sep=' ')
    print (a - b, a - c, b - c, sep=' ')
    print (a * b, a * c, b * c, sep=' ')
    
if __name__ == '__main__':
    main()