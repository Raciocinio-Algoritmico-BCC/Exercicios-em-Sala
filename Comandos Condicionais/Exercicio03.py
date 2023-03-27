# armazenando um inteiro digitado pelo usuário na variável pdl
pdl = int(input("Digite seu PdL: "))

# começo a fazer a verificação da variável pdl
# fazemos a estrutura com if, elif e else para que quando o programa
# encontre a condição correta, ele não verifique as demais condições
# isso torna nosso programa mais "barato" computacionalmente
# economizando processamento e tempo de espera
if pdl <= 999:
    print("Seu elo é ferro!")
elif pdl <= 1999:
    print("Seu elo é bronze!")
elif pdl <= 2999:
    print("Seu elo é prata!")
elif pdl <= 3999:
    print("Seu elo é ouro!")
elif pdl <= 4999:
    print("Seu elo é platina!")
elif pdl <= 5999:
    print("Seu elo é diamante!")
elif pdl <= 6999:
    print("Seu elo é mestre!")
elif pdl <= 7999:
    print("Seu elo é grão-mestre!")
else:
    print("Seu elo é desafiante!")