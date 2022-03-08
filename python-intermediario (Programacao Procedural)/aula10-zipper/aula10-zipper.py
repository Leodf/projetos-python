"""
Zip - Unindo iteráveis
Zip_longest - Intertools
"""
from itertools import zip_longest, count


### Código
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

# só vai unir a menor lista com o zip
cidades_estados = zip(estados, cidades)

# print(cidades_estados)
# print(list(cidades_estados))

# cidades_estados = zip_longest(indice,estados, cidades, fillvalue='Estado')
cidades_estados = zip(
    indice,
    estados, 
    cidades,
    )
# print(cidades_estados)
# print(list(cidades_estados))

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)