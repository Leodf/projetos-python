"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

nome =  'Leonardo'
print(f'{nome:s}')

num_3 = 1
print(f'{num_3:0>10}')

num_4 = 1250
print(f'{num_4:0>10}')
print(f'{num_4:0<10}')
print(f'{num_4:0^10}')
print(f'{num_4:0>10.2f}')

nome2 = 'Leonardo de Faveri'
print(f'{nome2:#^50}')

nome_formatado = '{:@>20}'.format(nome2)
print(nome_formatado)
nome_formatado = '{n}{n}{n}{n}'.format(n=nome2)
print(nome_formatado)
nome_formatado = '{n:0<20}'.format(n=nome2)
print(nome_formatado)