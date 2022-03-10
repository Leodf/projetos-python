
from dados import pessoas, produtos, lista

# nova_lista = filter(lambda x: x > 5, lista)
# nova_lista = [x for x in lista if x > 5]

# print(list(nova_lista))
"""
def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True
        return True

#lambda p: p['preco'] > 50
nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)
"""

def filtra(pessoa):
    if not pessoa['idade'] >= 18:
        return True
    else:
        return False

nova_lista = filter(filtra, pessoas)

for pessoas in nova_lista:
    print(pessoas)
