from collections import deque
import matplotlib.pyplot as plt
import numpy as np

# Laberinto representado como una matriz
# 0 = espacio libre, 1 = muro
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

# Dirección de movimiento (arriba, abajo, izquierda, derecha)
direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def es_valido(x, y, laberinto, visitado):
    """Verifica si la posición (x, y) es válida para moverse"""
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0 and not visitado[x][y]

def bfs(laberinto, inicio, fin):
    """Implementación de BFS para encontrar el camino más corto en el laberinto"""
    # Crear una matriz de visitados para marcar los nodos visitados
    visitado = [[False for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
    
    # Cola para la BFS, almacenará las posiciones y el camino
    cola = deque([(inicio, [inicio])])
    visitado[inicio[0]][inicio[1]] = True

    while cola:
        (x, y), camino = cola.popleft()

        # Si llegamos al destino, devolvemos el camino
        if (x, y) == fin:
            return camino

        # Explorar las 4 direcciones posibles
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if es_valido(nx, ny, laberinto, visitado):
                visitado[nx][ny] = True
                cola.append(((nx, ny), camino + [(nx, ny)]))

    # Si no hay camino, retornamos None
    return None

# Definir el punto de inicio y el punto de destino
inicio = (0, 0)  # (Fila, Columna)
fin = (0, 4)     # (Fila, Columna)

# Ejecutar la búsqueda en anchura (BFS)
# camino = bfs(laberinto, inicio, fin)

# if camino:
#     print("Camino encontrado:", camino)
# else:
#     print("No se encontró un camino.")

laberinto_array = np.array(laberinto)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Usar imshow para mostrar la matriz
# cmap='gray' para usar una escala de grises
# vmin y vmax para definir los valores mínimo y máximo del colormap
cax = ax.imshow(laberinto_array, cmap='gray', vmin=0, vmax=1)

# Opcional: agregar una cuadrícula para visualizar mejor los puntos
ax.grid(which='both', color='black', linestyle='-', linewidth=2)

# Configurar los ticks para que coincidan con las líneas de la cuadrícula
ax.set_xticks(np.arange(-.5, len(laberinto[0]), 1))
ax.set_yticks(np.arange(-.5, len(laberinto), 1))
ax.set_xticklabels([])
ax.set_yticklabels([])

# Mostrar la cuadrícula
ax.grid(True)

# Mostrar la figura
plt.show()