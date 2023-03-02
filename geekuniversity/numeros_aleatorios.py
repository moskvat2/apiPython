import numpy as np

# Gerar uma matriz randômica de 1 a 60
matriz = np.random.randint(1, 61, size=(6, 10))

# Selecionar aleatoriamente seis números da matriz
seis_numeros = np.random.choice(matriz.flatten(), size=6, replace=False)

print(seis_numeros)