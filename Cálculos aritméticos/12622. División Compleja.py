def main():
    
    r1, i1, r2, i2 = map(int, input().split())
    
    d1 = ((r1 * r2) + (i1 * i2)) / (r2 ** 2 + i2 ** 2)
    d2 = ((r2 * i1) - (r1 * i2)) / (r2 ** 2 + i2 ** 2)
    
    print(f'{d1:.3f} {d2:.3f}')
    
if __name__ == '__main__':
    main()