"""
Operadores lógicos
and, or, not
in e not in
"""

# (verdadeiro E falso) = falso

# (verdadeiro ou falso) = verdadeiro

# operador not serve na maioria para checar variaveis vazias
a = ''
b = 0

if not a:
    print('preencha um valor')

if not b:
    print('preencha um valor')

# os operadores in e not in servem para checar se algo está ou não contido dentro de uma variável

nome = 'Leonardo'

if 'nar' in nome:
    print('existe')
else:
    print('nada a ver')

if 'asdas' not in nome:
    print('executei')
else:
    print('existe o texto')