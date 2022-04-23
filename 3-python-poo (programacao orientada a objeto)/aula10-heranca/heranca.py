"""
Associação - Usa | Agregação - Tem | Composição - É dono | Herança - É
"""
from classes import *

cliente1 = Cliente('Leonardo', 30)
print(cliente1.nome)
cliente1.falar()
cliente1.comprar()

aluno1 = Aluno('Maria', 54)
print(aluno1.nome)
aluno1.falar()
aluno1.estudar()

p1 = Pessoa('João', 35)
print(p1.nome)
p1.falar()