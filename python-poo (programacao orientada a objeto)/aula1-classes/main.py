
from pessoas import Pessoa

p1 = Pessoa('Leonardo', 30)
p2 = Pessoa('João', 25)

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

"""
p1.falar('POO')
p2.falar('Filmes')
p1.comer('Churrasco')
p2.comer('Sorvete')
"""

"""
p1.comer('maça')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('maça')
p1.parar_falar()
"""
