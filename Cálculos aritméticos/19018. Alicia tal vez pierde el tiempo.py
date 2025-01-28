def main():
    
    C, E, J, D = map(int, input().split())
    
    horasUsadas = (C + E + J + D)
    horasPerdidas = 24 - horasUsadas
    segundosPerdidos = horasPerdidas * 3600
    
    H = int(input())
    
    
    
    print(int(segundosPerdidos)," ", int(segundosPerdidos * (H / 24)))
    
if __name__ == '__main__':
    main()