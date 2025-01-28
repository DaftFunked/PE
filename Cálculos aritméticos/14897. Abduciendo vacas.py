def main():
    
    V, E, D =map(float, input().split())
    
    t = (E * D) / (E - V)
    
    print(t)
    
if __name__ == '__main__':
    main()