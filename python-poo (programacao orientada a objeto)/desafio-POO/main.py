"""
Exercício com abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco tem clientes e contas.

Dicas:
Criar a classe Cliente que herda da Classe Pessoa (Herança)
    pessoa tem nome e idade (com getters)
    Cliente Tem conta (Agregação da classe ContaCorrente ou ContaPoupança)
Criar classes ContaPoupança e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm Agencia, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (abstração e polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para Agregar classes de clientes e de contas (Agregação) 
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele Banco
    * checar se o cliente é daquele Banco
    * checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

from classes.banco import Banco
from classes.cliente import Cliente 
from classes.conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Leonardo', 30)
cliente2 = Cliente('Rose', 25)
cliente3 = Cliente('João', 65)

conta1 = ContaPoupanca(111, 254136, 0)
conta2 = ContaCorrente(222, 254136, 0)
conta3 = ContaPoupanca(121, 254136, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado')

print('##########')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado')
