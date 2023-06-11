# Faça as seguintes operações aritméticas com os valores de cada posição e armazene-as em variáveis:
    # 1. soma de [0][0] e [1][0]
    # 2. subtração de [2][2] e [2][1]
    # 3. multiplicação de [0][1] e [2][0]
    # 4. divisão de [1][2] e [0][2]

# Imprima todas as variáveis.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz[0][0] = 20
matriz[1][2] = 15
matriz[2][1] = 19

soma = matriz[0][0] + matriz[1][0]
sub = matriz[2][2] - matriz[2][1]
mult = matriz[0][1] * matriz[2][0]
div = matriz[1][2] / matriz[0][2]

print(f'Soma: {matriz[0][0]} + {matriz[1][0]} = {soma}')
print(f'Subtração: {matriz[2][2]} - {matriz[2][1]} = {sub}')
print(f'Multiplicação: {matriz[0][1]} * {matriz[2][0]} = {mult}')
print(f'Divisão: {matriz[1][2]} / {matriz[0][2]} = {div}')