# Escreva uma função chamada "imprime_diagonal" que recebe uma matriz de tamanho
# 3x3 preenchida com valores quaisquer, e imprime os valores na diagonal principal.

# definição da função imprime_diagonal que recebe como parâmetro uma matriz
def imprime_diagonal(matriz):
    # para cada indice entre 0, 1 e 2
    for i in range(3):
        # imprime os valores da matriz quando são iguais
        # note que os índices da diagonal principal de uma matriz são sempre iguais
        # matriz[0][0], matriz[1][1] e matriz[2][2]
        print(matriz[i][i])

# criamos uma matriz 3x3 com valores quaisquer  
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# chamamos a função imprime_diagonal passando a matriz como parâmetro
imprime_diagonal(matriz)