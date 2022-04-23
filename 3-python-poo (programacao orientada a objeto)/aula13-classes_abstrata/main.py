"""
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self):
        pass

class B(A):
    def falar(self):
        print('Falando.... B...')

a = B()
a.falar()
"""
from classes.contapoupanca import ContaPoupanca
from classes.contacorrente import ContaCorrente

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(6)

print('#'*50)
cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)