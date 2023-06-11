# Utilizando a mesma matriz da prática anterior, altere os valores nas seguintes posições:
    # 1. [0][0] para 20
    # 2. [1][2] para 15
    # 3. [2][1] para 19
    
# Imprima novamente a matriz das 3 formas solicitadas anteriormente.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz[0][0] = 20
matriz[1][2] = 15
matriz[2][1] = 19

print("\n1. Impressão simples")
print(matriz)

print("\n2. Impressão com um for")
for linha in matriz:
    print(linha)
    
print("\n3. Impressão com dois for's")
for i in range(3):
    for j in range(3):
        print(matriz[i][j])