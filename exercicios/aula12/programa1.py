"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

n = input('Digite um número inteiro: ')

try:
    n = int(n)
    print('é um número e inteiro')
    if n % 2 == 0:
        print('O número digitado é par')
    else:
        print('O número digitado é ímpar')
except:
    print('Não é um inteiro')
    print(type(n))


