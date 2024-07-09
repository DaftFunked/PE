C, E, J, D = map(int, input().split())
H = int(input())

# 24 hrs
HT = C + E + J + D
HR = 24 - HT
SP = HR * 3600

print(SP, " ", int(SP * (H / 24)))     