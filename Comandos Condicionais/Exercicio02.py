# Leia a média de um estudante 
# e imprima se ele foi aprovado

# armazenando um numero real digitado pelo usuário na variável media
media = float(input("Digite a média do aluno: "))

# se a media for maior ou igual a 7 
if media >= 7:
    # imprime para o usuário que ele foi aprovado com média X
    print(f'Você foi aprovado com média {media}.')
# se a média não for maior ou igual a 7 (menor que 7)
else:
    # imprime para o usuário que ele foi reprovado com média X
    print(f'Você foi reprovado com média {media}.')