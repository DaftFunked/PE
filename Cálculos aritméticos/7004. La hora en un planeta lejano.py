S = int(input())

sm = 50
sh = 70 * sm
sd = 12 * sh

d = S // sd
S %= sd

h = S // sh
S %= sh

m = S // sm
s = S % sm

print(d, " ", h, " ", m, " ", s)