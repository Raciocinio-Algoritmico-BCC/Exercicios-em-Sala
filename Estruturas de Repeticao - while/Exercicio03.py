# Implemente um programa em Python para ler do teclado números.
# Caso o usuário forneça um número igual a -1, o programa deve
# fornecer a média dos números e encerrar;

# Variáveis auxiliares para a correta execução do programa
# soma é onde iremos armazenar a soma acumulada dos valores digitados
# contador é onde iremos armazenar a quantidade de valores digitados
contador = 0
soma = 0

# Enquanto meu programa estiver rodando
while True:
    # Peço input para o usuário
    numero = int(input("Digite um numero: "))

    # Verifico se o número é igual a -1
    if numero == -1:
        # Se for, imprimo a média para o usuário
        print(f'A média é igual {soma / contador}')
        # "Quebro" o loop, ou seja, paro de executar o while, ignorando qualquer código abaixo
        break

    # Caso o número não seja igual a -1
    # Acrescento o valor de numero à variável soma
    soma += numero
    # Conto mais 1 número digitado para a variável contador
    contador += 1


# Solução do Enrico que também funciona super bem!

# while numero != -1:
#     numero = int(input("Digite um numero: "))
#
#     if numero == -1:
#         print(f'A média é igual {soma / contador}')
#     else:
#         print("------------------")
#         soma += numero
#         # soma = soma + numero
#         contador += 1
#         # contador = contador + 1
