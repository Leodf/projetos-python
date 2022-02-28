# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

# muito similar ao dicionario mas é um set
# s1 = {1,2,3,4,5,6,7,8,9}

"""
s1 = set()
s1.add(1)
s1.add(2)
s1.discard(2)
print(s1)
"""
"""
# O set não mostra em ordem os elementos e com a função update ele é iterável
s1 = set()
s1.update('Python')

print(s1)
"""
"""
lista = [1,2,1,1,6,8,8,9,7,7,5,6,3,2,1,4,5,7,8,4,5,6,'Leo','Leo']
lista = set(lista)
lista = list(lista)
print(lista)
"""
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2
print(s3)
s3 = s1 & s2
print(s3)
s3 = s1 - s2
print(s3)
s3 = s2 - s1
print(s3)
s3 = s1 ^ s2
print(s3)
