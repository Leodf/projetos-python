"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. Ex: Bom dia 0:11, Boa tarde 12:17 e Boa noite 18:23.
"""

print('Programa de saudação')
hora = input('Qual hora do dia é? ')
minuto = input('Quantos minutos? ')

if hora.isnumeric() and minuto.isnumeric():
    if hora == 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11:
        print(f'Bom dia!! Agora são {hora} horas e {minuto} minutos')
    elif hora == 12 or 13 or 14 or 15 or 16 or 17:
        print(f'Boa tarde!! Agora são {hora} horas e {minuto} minutos')
    elif hora == 18 or 19 or 20 or 21 or 22 or 23:
        print(f'Boa noite!! Agora são {hora} horas e {minuto} minutos')
    else:
        print(f'A hora {hora}:{minuto} não existe')
else:
    print('voce digitou um caractere errado tente novamente')