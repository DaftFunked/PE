c, N = map(int, input().split())

if N > 8 or N < 0:
    print("ERROR")
else:
    if c == 0 and N != 3:
        c = 0
    elif c == 0 and N == 3:
        c = 1
    elif c == 1 and (N < 2 or N > 3):
        c = 0
    elif c == 1 and (N == 2 or N == 3):
        c = 1
        
    print(c)