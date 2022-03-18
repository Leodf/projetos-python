
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        print('Estou em Cliente')

class ClienteVIP(Cliente):
    """
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print('Outra coisa qualquer...')
    """
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade) # ou super().__init__(nome, idade)
        self.sobrenome = sobrenome
    
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')