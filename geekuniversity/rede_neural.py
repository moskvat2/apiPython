import numpy as np

# Definindo a função de ativação (degrau unitário)
def step_function(x):
    if x < 0:
        return 0
    else:
        # print(inputs)
        return 1

# Definindo uma função para treinar a rede neural perceptron
def train_perceptron(inputs, targets, weights, learning_rate, num_epochs):
    for epoch in range(num_epochs):
        for i in range(len(inputs)):
            x = inputs[i]
            y = step_function(np.dot(x, weights))
            error = targets[i] - y
            weights = weights + (learning_rate * error * x)
    return weights

# Gerando um conjunto de entradas aleatórias entre 1 e 60
inputs = np.random.randint(1, 61, (100, 60))

# Definindo um vetor de pesos aleatórios
weights = np.random.rand(60)

# Gerando um conjunto de saídas aleatórias para treinamento
targets = np.random.randint(0, 2, 100)

# Treinando a rede neural perceptron
learning_rate = 0.1
num_epochs = 100
weights = train_perceptron(inputs, targets, weights, learning_rate, num_epochs)

# Gerando um novo conjunto de entradas para teste
new_inputs = np.random.randint(1, 61, (10, 60))

# Usando a rede neural perceptron treinada para prever as saídas correspondentes
for i in range(len(new_inputs)):
    x = new_inputs[i]
    y = step_function(np.dot(x, weights))
    print("Entrada: {}, \nSaída: {}\n".format(x, y))
