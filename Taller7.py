import numpy as np

# Definimos una matriz cuadrada (por ejemplo)
matriz = np.array([[3, -1], [-2, 4,]])

# Calculamos los valores propios y los vectores propios
autovalores, autovectores = np.linalg.eig(matriz)

print("Valores propios:", autovalores)
print("Vectores propios:", autovectores)
