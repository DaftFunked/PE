def main():
    C = int(input())
    
    K = int(C + 273.15)
    F = int((C * 9/5) + 32)
    R = int(C * 0.8)
    
    print (K, F, R)
    
if __name__ == '__main__':
    main()