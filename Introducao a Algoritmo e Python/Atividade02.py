# ---------- PEGANDO INPUT DO USUÁRIO ----------
# peso e altura são medidas decimais portanto
# na hora de armazenar os valores nas variáveis
# é preciso converter o texto digitado para número real (float)
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

# o cálculo do IMC é dado pela fórmula: peso / altura²
# podemos realizar o cálculo de 3 formas:

# 1. A mais simples, onde dividimos o peso pela altura * altura
imc = peso / (altura * altura)

# 2. Utilizando o operador ** que é matemáticamente representado por altura²
# imc = peso / (altura ** 2)

# 3. Utilizando o operador ^ que é matemáticamente representado por altura²
# imc = peso / (altura ^ 2)

# ---------- IMPRIMINDO INFORMAÇÕES NO TERMINAL ----------
# podemos imprimir o valor cálculado da forma que já conhecemos
# concatenando (juntando) um texto informativo com a variável imc convertida para o tipo string
# nesta impressão o número irá sair completo, com várias casas decimais após o ponto
print("O seu IMC é: " + str(imc))

# ou podemos imprimir o valor utilizando o format do python
# que é representado por um f ANTES das áspas
# neste formato podemos inserir qualquer variável dentro de chaves {qualquerVariavel}
# se quisermos imprimir com apenas 2 números decimais após o ponto
# basta adicionar :.2f após o nome da variável dentro das chaves
# perceba que não é preciso converter a variável para string neste caso
print(f"O seu IMC é {imc:.2f}")