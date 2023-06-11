# Escreva uma função chamada "media" que receba uma lista de números como
# parâmetro e retorne a média desses números.

# definição da função media, que recebe como parâmetro números quaisquer
def media(numeros):
    # retorna a soma de todos os numeros da lista, dividido pelo tamanho da lista
    return sum(numeros) / len(numeros)

# imprime o retorno da média da lista com os valores 2, 4 e 6
print(media([2, 4, 6]))