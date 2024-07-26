I, D = map(int, input().split())

movimientos = (D - I) % 5

rueda = [1, 2, 3, 4, 5]

if movimientos > 0:
    numero_movido = rueda[0]
    rueda[0] = rueda[4]
    rueda[4] = rueda[3]
    rueda[3] = rueda[2]
    rueda[2] = rueda[1]
    rueda[1] = numero_movido

elif movimientos < 0:
    numero_movido = rueda[4]
    rueda[4] = rueda[0]
    rueda[0] = rueda[1]
    rueda[1] = rueda[2]
    rueda[2] = rueda[3]
    rueda[3] = numero_movido

for num in rueda:
    print(num, end=" ")
