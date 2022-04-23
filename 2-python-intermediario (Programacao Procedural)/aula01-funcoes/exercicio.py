"""
Crie uma função que exibe uma saudação com os parâmetros saudação e nome.
"""
from cmath import nan


def saudacao(msg, nome):
    print(msg, nome)

saudacao('Bom dia', 'Leonardo')

"""
Crie uma função que recebe 3 números com parâmetros e exiba a soma entre eles
"""
def soma(n1, n2, n3):
    print(n1+n2+n3)

soma(1,2,3)

"""
Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%). Retorne (return) o valor do primeiro numero somado do aumento do percentual do mesmo.
"""
def aumento(valor,percentagem):
    if percentagem < 0:
        return
    percentagem = percentagem / 100
    variacao = valor * (1 + percentagem)
    return print(f'O valor de {valor} foi aumentado em {percentagem*100}% e o novo valor foi para {variacao}')

aumento(10, 20)

"""
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da funçõa for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o número enviado.
"""
def fizzbuzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return print('fizzbuzz')
    if n % 3 == 0:
        return print('fizz')
    if n % 5 == 0:
        return print('buzz')
    return print(n)   

for i in range(101):
    fizzbuzz(i)