import math

def main():
    
    x, y, z = map(float, input().split())
    
    valor = (7 + (pow((2 * x + y - z), (2 * x + y - z)))) / (2 * x + y - z)
    
    print(valor)
    
if __name__ == '__main__' :
    main()