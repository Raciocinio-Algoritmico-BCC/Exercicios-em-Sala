# Escreva uma função chamada "inverter" que receba uma string como parâmetro e
# imprime a string invertida.

# Exemplo 1
# definição da função inverter, que recebe como parâmetro um valor qualuqer
def inverter1(texto):
    # retorno da junção de uma string vazia com o texto invertido pela função reversed
    return ''.join(reversed(texto))

# Exemplo 2
def inverter2(texto):
    # retorna o texto invertido
    # [::-1] é usado para indicar que queremos começar a percorrer o texto do fim, até o começo
    # movendo -1, indicando que estamos decrementando (diminuindo) 1 
    # no caso do texto 'MARINA' começamos pelo fim (letra A) e diminuímos 1, indo para letra N, I
    # ... e assim por diante
    return texto[::-1]

# imprime o retorno da função inverter (pode ser 1 ou 2, o resultado é o mesmo)
print(inverter2('MARINA'))