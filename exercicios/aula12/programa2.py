"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex: Bom dia 0:11, Boa tarde 12:17 e Boa noite 18:23.
"""

print('Programa de saudação')
hora = input('Qual hora do dia é? ')
minuto = input('Quantos minutos? ')

if hora.isnumeric() and minuto.isnumeric():
    if int(hora) >= 0 and int(hora) < 12 and int(minuto) < 60:
        print(f'Bom dia!! Agora são {hora} horas e {minuto} minutos')
    elif int(hora) >= 12 and int(hora) < 18 and int(minuto) < 60:
        print(f'Boa tarde!! Agora são {hora} horas e {minuto} minutos')
    elif int(hora) >= 18 and int(hora) < 24 and int(minuto) < 60:
        print(f'Boa noite!! Agora são {hora} horas e {minuto} minutos')
    else:
        print(f'A hora {hora}:{minuto} não existe, rode o programa novamente!')
else:
    print('voce digitou um caractere errado tente novamente')