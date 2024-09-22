def generar_secuencia(N):
    # Definir el patrón básico
    secuencia = [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5]
    
    # Inicializar la lista resultado
    resultado = []
    
    # Generar la secuencia
    while len(resultado) < N:
        resultado.extend(secuencia)  # Añadir el patrón a resultado
    
    # Recortar la lista para que tenga exactamente N elementos
    resultado = resultado[:N]
    
    # Imprimir los primeros N elementos
    print(" ".join(map(str, resultado)))

# Leer el valor de N
N = int(input())

# Generar la secuencia
generar_secuencia(N)
