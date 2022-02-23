"""
Crie uma função 1 que recebe uma função 2 como parâmetro e retorne o valor da função2 executada.
"""

def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)

"""
Crie uma função1 que recebe uma função2 como parametro e retorne o valor da funcçao2 executada. Faça a função 1 executar duas funções que recebam um numero diferente de argumentos
"""

def funcmestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def falar_oi(nome):
    return f'Oi {nome} '

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executar = funcmestre(falar_oi, 'Leo')
executar2 = funcmestre(saudacao, 'Leo', saudacao='Bom dia')
print(executar)
print(executar2)