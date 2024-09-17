def main():
    a, b, n = map(int, input().split())
    suma = 0
    for i in range(a, b + 1):
        potencia = pow(i, n)
        suma += potencia
        
    print(suma)
    
if __name__ == '__main__':
    main()