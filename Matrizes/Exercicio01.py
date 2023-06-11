# Crie uma matriz de tamanho 3x3 e preencha-a com valores de 1 a 9.
# Imprima a matriz das três formas:
    # 1. print(matriz)
    # 2. utilizando um for.
    # 3. utilizando dois for’s.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\n1. Impressão simples")
print(matriz)

print("\n2. Impressão com um for")
for linha in matriz:
    print(linha)
    
print("\n3. Impressão com dois for's")
for i in range(3):
    for j in range(3):
        print(matriz[i][j])