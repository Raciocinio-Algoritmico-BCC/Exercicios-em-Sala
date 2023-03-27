#Leia a idade do usuário e imprima 
# se ele pode tirar a carteira de habilitação

# armazenando um inteiro digitado pelo usuário na variável idade
idade = int(input("Digite a sua idade: "))

# se a idade for maior ou igual a 18 (se o usuário for maior de idade)
if idade >= 18:
    # imprime que ele já pode tirar a carteira de habilitação
    print("Você já pode tirar a sua carteira!")
# caso a idade dele não seja maior ou igual a 18 (se o usuário for menor de idade)
else:
    # imprime que ele não pode tirar a carteira de habilitação
    print("Você não pode tirar a carteira")