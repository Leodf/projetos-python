"""
For / Else em Python
"""

variavel = ['Leonardo', 'AJoaozinho', 'Maria']

for valor in variavel:
    print(valor)
    if valor.lower().startswith('j'):
        print(f'{valor} começa com J.')
        break
else:
    print('Não existe uma palavra que começa com J.')