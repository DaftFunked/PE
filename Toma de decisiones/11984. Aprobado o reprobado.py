def main():
    
    E1, E2, E3 = map(float, input().split())
    T1, T2, T3 = map(float, input().split())
    
    E = (E1 + E2 + E3) / 3
    
    T = (T1 + T2 + T3) / 3
    
    EP = E * 0.4
    TP = T * 0.6
    
    P = EP + TP
    
    if P >= 6 and E >= 6:
        print('aprobado', P)
    else:
        print('reprobado')
        
if __name__ == '__main__':
    main()