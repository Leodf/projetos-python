"""
* Criar variáveis para nome (str), idade (int),
* Altura (float) e peso (float) de uma pessoa.
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome='Leonardo'
idade = 30
altura = 1.85
peso = 95
imc = peso / (altura ** 2)
ano_atual = 2022
ano_nasc = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} kg.\nO IMC de {nome} é {imc:.2f}.\n{nome} nasceu em {ano_nasc}.')