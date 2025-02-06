def main():
    
    F = int(input())
    
    C = (F - 32) * 5 // 9
    
    if C <= 36:
        E = 0
    elif C > 36:
        E = 1
    
    print(C,"",E)
    
if __name__ == "__main__":
    main()