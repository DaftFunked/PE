# Función para calcular las reservas diarias de combustible
def calcular_reserva_semanal(L, N, l, m, w, j, v, s, d):
    # Variables para almacenar las reservas diarias
    reserva_lunes = 0
    reserva_martes = 0
    reserva_miercoles = 0
    reserva_jueves = 0
    reserva_viernes = 0
    reserva_sabado = 0
    reserva_domingo = 0
    
    # Lunes
    combustible_consumido_lunes = l * N
    if combustible_consumido_lunes > L:
        reserva_lunes = combustible_consumido_lunes - L
    
    # Martes
    L_martes = L + reserva_lunes
    combustible_consumido_martes = m * N
    if combustible_consumido_martes > L_martes:
        reserva_martes = combustible_consumido_martes - L_martes
    
    # Miércoles
    L_miercoles = L_martes + reserva_martes
    combustible_consumido_miercoles = w * N
    if combustible_consumido_miercoles > L_miercoles:
        reserva_miercoles = combustible_consumido_miercoles - L_miercoles
    
    # Jueves
    L_jueves = L_miercoles + reserva_miercoles
    combustible_consumido_jueves = j * N
    if combustible_consumido_jueves > L_jueves:
        reserva_jueves = combustible_consumido_jueves - L_jueves
    
    # Viernes
    L_viernes = L_jueves + reserva_jueves
    combustible_consumido_viernes = v * N
    if combustible_consumido_viernes > L_viernes:
        reserva_viernes = combustible_consumido_viernes - L_viernes
    
    # Sábado
    L_sabado = L_viernes + reserva_viernes
    combustible_consumido_sabado = s * N
    if combustible_consumido_sabado > L_sabado:
        reserva_sabado = combustible_consumido_sabado - L_sabado
    
    # Domingo
    L_domingo = L_sabado + reserva_sabado
    combustible_consumido_domingo = d * N
    if combustible_consumido_domingo > L_domingo:
        reserva_domingo = combustible_consumido_domingo - L_domingo
    
    # Devolver las reservas diarias como una tupla
    return (reserva_lunes, reserva_martes, reserva_miercoles, reserva_jueves, reserva_viernes, reserva_sabado, reserva_domingo)

# Leer los datos de entrada directamente
datos = input().split()
L = int(datos[0])
N = int(datos[1])
l = int(datos[2])
m = int(datos[3])
w = int(datos[4])
j = int(datos[5])
v = int(datos[6])
s = int(datos[7])
d = int(datos[8])

# Calcular las reservas diarias
reservas_diarias = calcular_reserva_semanal(L, N, l, m, w, j, v, s, d)

# Imprimir resultados
print(" ".join(map(str, reservas_diarias)))
