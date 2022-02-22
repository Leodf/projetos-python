"""
Continuação do Enumerate
"""

lista = [
    #  0       1       2
    ['Edu', 'João', 'Luiz'], # 0
    ['Maria', 'Aline', 'Joana'], # 1
    ['Helena', 'Leonardo', 'Silva'], # 2
]
enumerada = list(enumerate(lista))
print(enumerada[1][1][2])

"""
[ <-- Enumerate

São Tuplas
    #0            # 1
    (0, ['Edu', 'João', 'Luiz']), # 0
            0       1       2
    (1, ['Maria', 'Aline', 'Joana']),  # 1
    (2, ['Helena', 'Leonardo', 'Silva'])  # 2


"""