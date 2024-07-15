a, b = map(int, input().split())

A = 534 // a
B = 534 // b

if (534 % a != 0):
    A += 1
if (534 % b != 0):
    B += 1
    
if (A < B):
    print("A", " ", A)
else:
    print("B", " ", B)