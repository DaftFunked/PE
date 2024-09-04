def main():
    
    pares = 0
    impares = 0
    sumapar = 0
    sumaimpar = 0
    
    N = int(input())
    
    numeros = list(map(int, input().split()))
    
    for numero in numeros:
        
        if numero % 2 == 0:
            pares += 1
            sumapar += numero
        else:
            impares += 1
            sumaimpar += numero
            
    prom_par = 0
    if pares != 0:
        prom_par = sumapar / pares
        
    prom_impar = 0
    if impares != 0:
        prom_impar = sumaimpar / impares
        
    if prom_par > prom_impar:
        ganador = "APARICIO"
    elif prom_par < prom_impar:
        ganador = "NONILA"
    else:
        ganador = "EMPATE!"
        
    print(ganador)
    

if __name__ == "__main__":
    main()