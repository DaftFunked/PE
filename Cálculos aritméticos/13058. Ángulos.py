def main():
    n = int(input())
    
    if n > 360:
        cociente = n // 360
        resto = n - (360 * cociente)
        print (resto)
    else:
        print (n)
        
if __name__ == '__main__':
    main()