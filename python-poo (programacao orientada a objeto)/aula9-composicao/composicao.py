
from classes import Cliente

print("#"*100)
cliente1 = Cliente('Leonardo', 30)
cliente1.insere_endereco('São Paulo', 'SP')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 25)
cliente2.insere_endereco('Belo Horizonte', 'MG')
cliente2.insere_endereco('Salvador', 'Bahia')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('João', 20)
cliente3.insere_endereco('Curitiba', 'PR')
cliente3.insere_endereco('Rio e Janeiro', 'RJ')
cliente3.insere_endereco('Recife', 'PE')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3
print()
print('#'*100)