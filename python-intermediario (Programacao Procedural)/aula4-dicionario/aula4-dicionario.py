
"""
# criando dicionario
d1 = {'chave1': 'valor da chave'}
d1['nova_chave'] = 'Valor da nova Chave'

print(d1['chave1'])
print(d1)

# outra maneira de criar o dicionario
d2 = dict(chave2='Valor da chave', chave3='Valor outra chave')
print(d2)

d3 = {
    'str': 'valor',
    123: 'Outro valor',
    (1,2,3,4):'Tupla',
}

d3['str'] = 'Agora ela existe'

print(d3)

if d3.get('str') is not None:
    print(d3.get('str'))

print(123)
"""

d1 = {
    'str': 'Valor',
    123: 'Outro Valor',
    (1,2,3,4) : 'Tupla',
}

print('str' in d1)
print('str' in d1.keys())
print('Valor' in d1.values())
