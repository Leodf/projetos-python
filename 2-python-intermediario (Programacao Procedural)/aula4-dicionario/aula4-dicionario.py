
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


d1 = {
    'chave1': 'Valor',
    'chave2': 'Outro Valor',
    'chave3': 'Tupla',
}

print('str' in d1)
print('str' in d1.keys())
print('Valor' in d1.values())

print(len(d1))

for k, v in d1.items():
    #print(k)
    #print(k[0], k[1])
    print(k, v)
"""

clientes = {
    'cliente1':{
        'nome': 'Leonardo',
        'sobrenome':'de Faveri',
    },
    'cliente2':{
        'nome': 'João',
        'sobrenome':'Moreira',
    },
    'cliente3':{
        'nome': 'Maria',
        'sobrenome':'Moreira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')