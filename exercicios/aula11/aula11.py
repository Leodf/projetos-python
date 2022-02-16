"""
função Len
"""

usuario = input('Digite seu usuário: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Voce precisa digitar 6 caracteres')
else:
    print('voce foi cadastrado')