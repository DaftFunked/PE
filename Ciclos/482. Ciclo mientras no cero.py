def main():
    
    suma = 0
    numeros = list(map(int, input().split())) 
    
    for n in numeros:
        suma += n
        if n == 0:
            break
        
    print(suma)
    
if __name__ == "__main__":
    main()