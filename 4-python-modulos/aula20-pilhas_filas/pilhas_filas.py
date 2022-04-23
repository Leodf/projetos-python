"""
Pilhas e filas
Pilha (stack) - LIFO - last in, first out.
    Exemplo: Pilha de livros que são adicionados um sobre o outro
Fila (queue) - FIFO - first in, first out.
    Exemplo: Uma fila de banco (ou qualquer fila da vida real)
Filas podem ter efeitos colaterais em desempenho, porque a cada item alterado, todos os indices serão modificados
"""
"""
livros = list()
livros.append('Livro 1')
livros.append('Livro 2')
livros.append('Livro 3')
livros.append('Livro 4')
livros.append('Livro 5')
print(livros)
livro_removido = livros.pop()
print(livros, livro_removido)
"""

from collections import deque
from time import sleep
"""
fila = deque()
fila.append('Joãozinho')
fila.append('Maria')
fila.append('Luiz')
fila.append('José')
print(fila)
print(f'Saiu: {fila.popleft()}')
"""
"""
fila = deque(maxlen=5)
fila.extend([1,2,3,4])
fila.append(5)
fila.append(6)

print(fila)
"""
fila = deque(maxlen=10)

for i in range(100):
    fila.append(i)
    sleep(.2)
    print(fila)