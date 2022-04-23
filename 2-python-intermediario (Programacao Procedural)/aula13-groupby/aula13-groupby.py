
from itertools import groupby, tee

alunos = [
    {'nome': 'Leonardo', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'B'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'João', 'nota': 'D'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'Silvio', 'nota': 'A'},
    {'nome': 'Carlos', 'nota': 'B'},
    {'nome': 'Helena', 'nota': 'D'},
]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')
    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))
    print(f'{quantidade} alunos tiraram a nota {agrupamento}')
    print()