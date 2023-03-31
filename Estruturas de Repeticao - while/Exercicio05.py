# Escreva um programa que receba 10 números do teclado e exiba a
# quantidade de números pares e ímpares lidos

# Variáveis auxiliares
# Contador para controlar a quantidade de números digitados
contador = 0
# Variável para contar quantos números pares foram digitados
numeroPar = 0
# Variável para contar quantos números ímpares foram digitados
numeroImpar = 0

# Enquanto o contador for menor que 10
# O loop vai ser executado 10x, pois o contador começa em 0 e e vai até 9
# Perceba que o 0 foi incluído na contagem, por isso que de 0 a 9 são 10x
while contador < 10:
    # Solicita um valor inteiro ao usuário
    a = int(input("Digite um numero: "))
    # Conta + 1 para o contador
    contador += 1

    # Se o resto da divisão do número digitado por 2 for == 0
    # Significa que o número é par
    if a % 2 == 0:
        # Contamos um para a variável de número par
        numeroPar += 1
        # numeroPar = numeroPar + 1
    # Caso contrário, o resto da divisão por 2 NÃO FOR igual a 0
    # Significa que o número é ímpar
    else:
        # Contamos um para a variável número impar
        numeroImpar += 1

# Fora do loop imprimimos o resultado para o usuário
print(f'A quantidade de números pares é {numeroPar}')
print(f'A quantidade de números ímpares é {numeroImpar}')