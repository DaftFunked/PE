import math

def main():
    x, y, z = map(float, input().split())
    
    resultado = (x + x * (y + z ** 2)) / ((x + math.pi) * (y + math.pi))
    
    print (resultado)
    
if __name__ == '__main__':
    main()