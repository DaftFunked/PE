def main():
    
    N = int(input())
    nidos = list(map(int, input().split()))
    
    M = int(input())
    cambios = list(map(int, input().split()))
    
    alturaActual = 1
    
    nidosVisitados = set()
    
    for cambio in cambios:
        
        alturaActual += cambio
        
        if alturaActual in nidos:
            nidosVisitados.add(alturaActual)
            
    print(len(nidosVisitados))
    
if __name__ == '__main__':
    main()