def main():
    
    x, y, z = map(float, input().split())
    
    valor = ((((2 * x) + y) / z) * (y ** 3 - z)) / (((x + (2 * y) + (3 * z)) / (z - (2 * y) - (3 * x))) + x ** 2 + z ** 2)
    
    print(valor)
    
if __name__ == '__main__':
    main()