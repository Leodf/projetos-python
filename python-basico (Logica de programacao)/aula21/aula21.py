"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""
"""
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1=string.split(' ')
lista_2=string.split(',')

print(lista_1)
print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    #print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')
    qtde_vezes = lista_1.count(valor)  

    if qtde_vezes > contagem:
        contagem = qtde_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
"""
"""
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1=string.split(' ')
string_2 = ' '.join(lista_1)

print(string)
print(lista_1)
print(string_2)
"""
"""
string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1=string.split(' ')

for indice, valor in enumerate(lista_1):
    print(indice, valor, lista_1[indice])
"""
lista = [
    [0,'Leonardo'],
    [1,'João'],
    [2,'Maria'],
]

for indice, nome in lista:
    print(indice, nome)

lista_1 = ['Leonardo', 'João', 'Maria']

for indice, nome in enumerate(lista_1):
    print(indice, nome)

