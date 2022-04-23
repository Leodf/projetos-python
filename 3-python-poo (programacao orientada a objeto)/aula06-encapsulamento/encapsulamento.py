"""
public, protected, private
_ privado/protected (maneira mais fraca)
__ privado (_NOMECLASSE__nomeatributo)

"""

class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)    

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]

base = BaseDeDados()
base.inserir_cliente(1, 'Leonardo')
base.inserir_cliente(2, 'Miranda')
base.inserir_cliente(3, 'Rose')
base.__dados = 'Outra coisa'
# print(base.__dados)
# print(base._BaseDeDados__dados)
# base.lista_clientes()

base.dados = 'Outro valor'
print(base.dados)
