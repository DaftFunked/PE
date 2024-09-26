def main():
    
    N = int(input())
    
    parejas = []
    
    for _ in range(N):
        x, y = list(map(float, input().split()))
        parejas.append((x, y))
        
    maxArea = 0.0
    
    for i in range(N):
        for j in range(i + 1, N):  # j debe ser mayor que i
            for k in range(j + 1, N):  # k debe ser mayor que j
                p1 = parejas[i]
                p2 = parejas[j]
                p3 = parejas[k]
                
                
                area = abs(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2
                
                
                if area > maxArea:
                    maxArea = area
                    
    print(f"{maxArea:.3f}")
    
if __name__ == '__main__':
    main()