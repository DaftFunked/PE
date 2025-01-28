def main():
    
    x, y, z = map(float, input().split())
    
    valor = ((pow(x, 1.2 * y)) - z + 5.7) / ((x + (2 * y) + (3 * z)) / (x * y))
    
    print(valor)
    
if __name__ == '__main__':
    main()