# Imprima na tela a tabuada de um
# número inteiro lido pelo teclado

# Solicita ao usuário o número que será realizada a tabuada
numero = int(input("Digite um número: "))
# Cria uma variável para assumir o valor dos multiplicadores começando em 1
# Queremos que essa variável comece em 1 e vá até 10 para multiplicar pelo valor digitado pelo usuário
multiplicador = 1

# O multiplicador irá começar em 1 e o loop vai acontecer até que ele atinja o valor 10
while multiplicador <= 10:
    # Impressão no console do resultado da multiplicação
    print(f'{numero} x {multiplicador} = {numero * multiplicador}')
    # aumento em 1 a variável multiplicador (incremento)
    multiplicador += 1
    # multiplicador = multiplicador + 1