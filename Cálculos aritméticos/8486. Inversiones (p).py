x, tasa1, tasa2, tasa3, porcentaje = map(float, input().split())

inversion = int(x) / 3
ganancia1 = inversion * tasa1
ganancia2 = inversion * tasa2
ganancia3 = inversion * tasa3

ganancia_mensual = ganancia1 + ganancia2 + ganancia3
comision = porcentaje * ganancia_mensual
ganancia_anual = (ganancia_mensual * 12) - (comision * 12)
total = x + ganancia_anual

print(f"{total:.3f}".format(10/3))
