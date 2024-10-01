def main():
    
    N = int(input())
    
    numeros = set()
    llamadas = {}
    
    maxLlamandas = 0
    numeroMasLlamado = 0
    
    for _ in range(N):
        telefono = int(input())
        
        if telefono not in numeros:
            numeros.add(telefono)
            
        if telefono in llamadas:
            llamadas[telefono] += 1
        else:
            llamadas[telefono] = 1
            
            
        if llamadas[telefono] > maxLlamandas:
            maxLlamandas = llamadas[telefono]
            numeroMasLlamado = telefono
            
    print(maxLlamandas, numeroMasLlamado)
    
    
if __name__ == '__main__':
    main()