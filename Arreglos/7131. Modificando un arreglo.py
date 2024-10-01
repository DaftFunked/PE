def main():
    
    N, M = map(int, input().split())
    
    arreglo = [0] * N
    
    for _ in range(M):
        index = int(input())
        arreglo[index] += 1
        
    print(" ".join(map(str, arreglo)))
    
if __name__ == '__main__':
    main()