# Escreva uma função chamada "maior" que receba três números como parâmetros e
# retorne o maior entre eles.

def maior(a, b, c):
    maior = a
    
    if b > maior:
        maior = b
    
    if c > maior:
        maior = c
        
    return maior

print(maior(18, 23, 10))