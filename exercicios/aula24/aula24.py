"""
Trocando o valor de variaveis
"""
from re import X


x = 10
y = 'Leonardo'

z = x
x = y
y = z

print(x, y, z)

# no python pode ser dessa maneira

x, y = y, x
print(x, y)

z = 'Faveri'
x, y, z = z, x, y

print(f'x={x} e y={y} e z={z}')