def suma_digitos(boleto):
    suma = 0
    while boleto > 0:
        suma += (boleto % 10)
        boleto //= 10
        
    return suma

def main():
    
    n = int(input())
    p = 0
    boleto = n
    
    while True:
        digitos = suma_digitos(boleto)
        
        if digitos == 21:
            break
        
        boleto += 1
        p += 1
        
        if boleto > 9999999:
            boleto = 0
            
    print(p, f"{boleto:07d}", end=" ")
    
if __name__ == '__main__':
    main()