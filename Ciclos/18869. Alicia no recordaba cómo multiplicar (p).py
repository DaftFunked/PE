A, B = map(int, input().split())

print(A, end="")
for i in range(1, B + 1):
    print("+", A, end="")
print("=", B, end="")
for i in range(1, A + 1):
    print("+", B, end="")