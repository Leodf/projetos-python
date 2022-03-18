
from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @classmethod
    def new_method(cls):
        pass

p1 = Pessoa('Leonardo', 1992)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento() 
