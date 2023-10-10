min_value = 5170.00
max_value = 5242.50

middle_point = (min_value + max_value) / 2
high_target = middle_point + (max_value - min_value) * 2.5
low_target = middle_point - (max_value - min_value) * 2.5

print("Ponto Médio:", middle_point)
print("Alvo de 250%/261.8% para cima:", high_target)
print("Alvo de 250%/261.8% para baixo:", low_target)
print("Fim")