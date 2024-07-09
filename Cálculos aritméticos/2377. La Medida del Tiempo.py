s = int(input())

sm = 60
sh = 60 * sm
sd = 24 * sh
sa = 365 * sd

a = s // sa
s %= sa

d = s // sd
s %= sd

h = s // sh
s %= sh

m = s // sm
q = s % sm

print(a, " ", d, " ", h, " ", m, " ", q)