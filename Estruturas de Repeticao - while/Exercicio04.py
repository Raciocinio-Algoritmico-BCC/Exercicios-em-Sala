# Implemente um programa em Python para imprimir na tela o
# somatório dos N primeiros números inteiros a partir do 1. Sendo N
# lido do teclado;

# Solução do colega Enzo

# Leio o valor do teclado
n = int(input("Digite um número inteiro: "))

# Crio variáveis para auxiliar durante o programa
# Soma vai acumular a soma dos primeiros números a partir do 1
soma = 0
# contador começar a partir do 1 (exercício pede a partir do 1)
contador = 1

# Enquanto o contador for menor ou igual ao número digitado
# Nesse exemplo estamos incluindo o 1, mas vai da interpretação de cada um
while contador <= n:
    # Incluimos o valor de contador à soma
    soma += contador
    # Aumentamos o valor do contador em 1
    contador += 1

# Impressão do resultado para o usuário
print(f'A soma dos {n} primeiro números inteiros é: {soma}')