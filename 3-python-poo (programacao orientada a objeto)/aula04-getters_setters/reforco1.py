
# SETTER = configurando um valor (=)
# GETTER = obter um valor (.)

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        print('Setter foi executado')
        nome += 'Sei la'
        self._nome = nome


p1 = Pessoa('Leonardo')
print(p1._nome)
print(p1.nome)