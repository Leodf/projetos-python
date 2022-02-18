"""
Faça um programa que peça o primeiro nome ao usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que seis letras "Seu nome é muito grande".
"""
print('Programa para contar as letras do seu nome')
nome = input('Digite seu primeiro nome:')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) >= 5 and len(nome) <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')