"""
Funções - def em Python (Parte 1)
"""

# As funções são úteis quando precisa repetir uma coisa mais de uma vez
def funcao():
    print('Olá mundo!')

funcao()
funcao()
funcao()
funcao()
print('Hello World!')
print('Hello World!')
print('Hello World!')
print('Hello World!')

# quando colocar um argumento precisa colocar o parametro dentro do parensteses
def funcao_1(msg):
    print(msg)

funcao_1('Mensagem')

def saudacao(msg = 'Olá', nome = 'usuário'):
    nome = nome.replace('e', '3')
    print(msg, nome)

saudacao()
saudacao(nome='zezinho', msg='Hi')
saudacao('Olá', 'Leonardo')
saudacao('Hello', 'Luiz')
saudacao('Oi', 'Maria')