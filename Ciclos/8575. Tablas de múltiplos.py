def main():
    A, B, N = map(int, input().split())
    
    temp_A = A
    temp_B = B
    
    while temp_B != 0:
        temp = temp_B
        temp_B = temp_A % temp_B
        temp_A = temp
        
    MCM = (A * B) // temp_A
    
    T = N // A + N // B - N // MCM
    
    max_A = (N // A) * A
    max_B = (N // B) * B
    
    M = max(max_A, max_B)
    
    print(T, " ", M)
    
if __name__ == "__main__":
    main()