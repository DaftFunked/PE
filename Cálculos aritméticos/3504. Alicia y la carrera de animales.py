def main():
    
    R, P = map(int, input().split())
    
    T = (P * R) / (P - R)
    
    print(T)
    
if __name__ == '__main__':
    main()