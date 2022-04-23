# Listas, dicionários (objetos mutáveis)
# Tuplas, strings, números, True, False, None (Imutável)

# Problema de parametro mutavel em função
"""
def lista_de_cliente(clientes_iteravel, lista=[]):
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_cliente(['joão', 'Maria', 'Eduardo'])
clientes2 = lista_de_cliente(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_cliente(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
"""
# Resolvendo o problema
def lista_de_cliente(clientes_iteravel, lista = None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_cliente(['joão', 'Maria', 'Eduardo'])
clientes2 = lista_de_cliente(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_cliente(['José'])

print(clientes1)
print(clientes2)
print(clientes3)
