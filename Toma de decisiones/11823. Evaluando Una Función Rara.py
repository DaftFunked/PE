def f (x):
    if (x <= 0):
        return pow(x,2) - x
    else:
        return -pow(x,2) + 3 * x
    
x = int(input())

print(int(f(x)))