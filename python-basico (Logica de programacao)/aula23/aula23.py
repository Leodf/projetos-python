"""
Desempacotamento de listas em python
"""

lista = ['Luiz', 'João', 'Maria', 1,2,3,4,5,6,8,7,8,100]

n1, n2, *outra_lista = lista

print(n1)
print(n2)
print(outra_lista)