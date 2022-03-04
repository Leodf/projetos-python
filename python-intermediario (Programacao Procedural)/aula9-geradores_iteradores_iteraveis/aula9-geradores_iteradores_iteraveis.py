
"""
lista = [0,1,2,3,4,5,6] # True
lista = 123456 # False
lista = 'String' # True

print(hasattr(lista, '__iter__')) # para saber se é iterável

# for v in lista:
    # print(v)

# para a lista se tornar um iterador
lista = iter(lista)
print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
"""

import sys
import time

# lista1 = list(range(1000))
# print(sys.getsizeof(lista1))

# Geradores vão acessar um dado específico a fim de evitar usar excessivamente a memória

# exemplificando uma tarefa pesada:
"""
def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

g = gera()

for v in g:
    print(v)

# Exemplificando o gerador
def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)
"""

l1 = [x for x in range(100000)]
print(type(l1))
print(sys.getsizeof(l1))
l2 = (x for x in range(100000))
print(type(l2))
print(sys.getsizeof(l2))

