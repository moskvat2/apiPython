import numpy as np
# Entradas:
entradas = np.array([[1, 0, 0, 0, 0, 0], #02
                     [1, 0, 1, 0, 0, 0], #08
                     [1, 1, 0, 0, 0, 0], #16
                     [1, 1, 1, 0, 0, 0], #24
                     [1, 0, 0, 1, 0, 0], #37
                     [1, 0, 0, 0, 1, 0]]) #43

# Saidas:
saidas = np.array([0, 1, 1, 1, 0, 1])

# Pesos:
pesos = np.array([0.2, 0.2, 0.2, 0.2, 0.2, 0.2])

# Taxa de Aprendizagem
taxa_aprendizagem = 0.5

def stepFunction(soma):
    if (soma >= 1):
        return 1
    return 0

def calculoSaida(registro):
    s = registro.dot(pesos)
    return stepFunction(s)

def treinar():
    erroTotal = 1
    while (erroTotal != 0):
        erroTotal = 0
        for i in range(len(saidas)):
            saidaCalculada = calculoSaida(np.asarray(entradas[i]))
            erro = abs(saidas[i] - saidaCalculada)
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxa_aprendizagem * entradas[i][j] * erro)
                print("Peso atualizado: " + str(pesos[j]))
        print("Total de erros: " + str(erroTotal))

treinar()

print("Rede neural perceptron treinada")
print(calculoSaida(entradas[0]))
print(calculoSaida(entradas[1]))
print(calculoSaida(entradas[2]))
print(calculoSaida(entradas[3]))
print(calculoSaida(entradas[4]))
print(calculoSaida(entradas[5]))