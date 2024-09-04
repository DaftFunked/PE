def main():
    
    N = int(input())
    
    calificaciones = list(map(int, input().split()))
    suma = 0
    promedio = 0
    
    for i in range(N):
        suma = suma + calificaciones[i]
        
    promedio = suma / N
    
    print(f"{promedio:.2f}")
    
if __name__ == "__main__":
    main()