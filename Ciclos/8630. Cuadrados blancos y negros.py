def actualizar_colores(n, colores):
    # Definir la tabla de actualización según los colores de los vecinos
    regla = {
        (0, 0, 0): 0,
        (0, 0, 1): 1,
        (0, 1, 0): 0,
        (0, 1, 1): 1,
        (1, 0, 0): 0,
        (1, 0, 1): 1,
        (1, 1, 0): 0,
        (1, 1, 1): 1
    }
    
    for _ in range(n):
        # Aplicar la regla para cada cuadrado, usando vecinos circulares
        nuevo_c1 = regla[(colores[2], colores[0], colores[1])]  # Vecinos del cuadrado 1: cuadrado 3 y cuadrado 2
        nuevo_c2 = regla[(colores[0], colores[1], colores[2])]  # Vecinos del cuadrado 2: cuadrado 1 y cuadrado 3
        nuevo_c3 = regla[(colores[1], colores[2], colores[0])]  # Vecinos del cuadrado 3: cuadrado 2 y cuadrado 1
        
        # Actualizar los colores
        colores = [nuevo_c1, nuevo_c2, nuevo_c3]
    
    return colores

# Leer la entrada
n = int(input())
colores = list(map(int, input().split()))

# Obtener los colores después de aplicar la regla n veces
resultado = actualizar_colores(n, colores)

# Imprimir el resultado
print(" ".join(map(str, resultado)))
