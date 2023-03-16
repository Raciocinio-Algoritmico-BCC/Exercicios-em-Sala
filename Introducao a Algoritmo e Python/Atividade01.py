# ---------- PEGANDO INPUT DO USUÁRIO ---------- 

# o usuário irá digitar um NOME que será armazenado na variável nome
# o texto digitado será armazenado no formato string (str)
nome = input("Digite o seu nome: ")
# o usuário irá digitar um CPF que será armazenado na variável cpf
# os números digitados serão armazenados no formato string (str)
cpf = input("Digite o seu CPF: ")
# o usuário irá digitar um TELEFONE que será armazenado na variável telefone
# os números digitados serão armazenados no formato string (str)
telefone = input("Digite o seu telefone: ")
# o usuário irá digitar um ANO que será armazenado na variável ano
# os números digitados serão armazenados no formato inteiro (int)
ano = int(input("Digite o seu ano de nascimento: "))

# obs: para dados como CPF e TELEFONE podemos armazenar como texto
# pois não iremos realizar nenhuma operação aritmética com este tipo de dado

# ---------- IMPRIMINDO INFORMAÇÕES NO TERMINAL ----------
# para imprimir informações que não são variáveis 
# sempre iremos usar áspas simples '' ou duplas ""
# para concatenar (juntar) strings (textos) usamos o sinal +
# variáveis do tipo string (str) não precisam ser convertidas na hora da impressão
print("O seu nome é " + nome)
print("O seu CPF é " + cpf)
print("O seu telefone é " + telefone)
# variáveis que NÃO SÃO strings (str) precisam ser convertidas na hora da impressão
# para converter qualquer variável para string basta fazer str(nomeDaVariavel)
print("O seu ano de nascimento é " + str(ano))