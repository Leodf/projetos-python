"""
Criando um sistema de perguntas e respostas com dicionarios
"""
print()
print('Jogo de perguntas e respostas')
print()
perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2+2',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta_certa': 'b',
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 3*2',
        'respostas': {'a': '4', 'b': '10', 'c': '6',},
        'resposta_certa': 'c',
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 7*7',
        'respostas': {'a': '49', 'b': '64', 'c': '45',},
        'resposta_certa': 'a',
    },
    'pergunta 4': {
        'pergunta': 'Quanto é 3+4',
        'respostas': {'a': '4', 'b': '7', 'c': '6',},
        'resposta_certa': 'b',
    },
    'pergunta 5': {
        'pergunta': 'Quanto é 5*5',
        'respostas': {'a': '8', 'b': '4', 'c': '25',},
        'resposta_certa': 'c',
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
    
    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('EHHHHHHH!!!! Você Acertou!!!!')
        respostas_certas += 1
    else:
        print('IIXXIIII!!!! Você Errou!!!!')
    print()

qtde_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtde_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')