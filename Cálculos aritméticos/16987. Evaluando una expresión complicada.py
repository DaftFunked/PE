import math

def main():
    
    x, y, z = map(float, input().split())
    
    valor = (pow((2 * y) + z, 2.8) - z) / (x + y - (x / z))
    
    print(valor)
    
if __name__ == '__main__'    :
    main()