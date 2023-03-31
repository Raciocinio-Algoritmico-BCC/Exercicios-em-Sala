# Implemente um programa em Python para
# 1. ler do teclado a nota de um aluno.
# Verifique se o valor lido é uma nota válida (maior que 7).
# Se não for, ler este valor até que a mesma seja válida;

# Leio do teclado o valor de nota
nota = float(input("Digite a nota do aluno: "))

# Enquanto a nota for inválida, ou seja:
# 1. menor ou igual a 7
# 2. menor que 0 (negativa)
# 3. maior que 10 (nota máxima)
while nota <= 7 or nota < 0 or nota > 10:
    # Informo que a nota digitada é invalida, e solicito uma nova nota
    nota = float(input("Nota inválida! Digite uma nota maior que 7.0 :"))

# Ao final imprimo a nota do aluno
print(f'A nota do aluno é {nota}')