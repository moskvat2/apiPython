import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

# Definindo a função de ativação
def step_function(x):
    return 1 if x >= 0 else 0

# Definindo a função para treinar a rede neural
def train_perceptron(X, y, learning_rate=0.1, epochs=100):
    # Adicionando uma coluna de 1s na matriz de entrada X
    X = np.insert(X, 0, 1, axis=1)
    # Inicializando os pesos com valores aleatórios
    weights = np.random.rand(X.shape[1])
    # Loop de treinamento
    for epoch in range(epochs):
        for i in range(X.shape[0]):
            x_i = X[i]
            y_i = y[i]
            y_hat = step_function(np.dot(x_i, weights))
            error = y_i - y_hat
            weights += learning_rate * error * x_i
    return weights

# Gerando dados de entrada e saída aleatórios
X = np.random.randint(1, 61, (100, 60))
y = np.random.randint(0, 2, 100)

# Treinando a rede neural
weights = train_perceptron(X, y)

# Plotando os pontos de entrada e a fronteira de decisão
cmap = ListedColormap(['red', 'blue'])
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap)
x_plot = np.array([1, 60])
y_plot = -(weights[0] + weights[1] * x_plot) / weights[2]
plt.plot(x_plot, y_plot)
plt.xlabel('Entrada 1')
plt.ylabel('Entrada 2')
plt.show()
