def main():
    
    P = int(input())
    babilonicos = []
    
    while P > 0:
        residuo = P % 60
        babilonicos.append(residuo)
        P //= 60
    
    resultado = []
    
    for d in babilonicos:
        
        decenas = d // 10
        unidades = d % 10
        
        babilonico = 'L' * decenas + 'I' * unidades
        
        resultado.append(babilonico)
        
        
    final = '.'.join(resultado)
    
    print(final)
    
if __name__ == '__main__':
    main()