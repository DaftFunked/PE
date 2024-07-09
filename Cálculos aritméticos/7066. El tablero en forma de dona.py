W, H, X, Y, R, S = map(int, input().split())

x = (X + R) % W

if x < 0:
    x += W

y = (Y + S) % H

if y < 0:
    y += H
    
print(x, " ", y)