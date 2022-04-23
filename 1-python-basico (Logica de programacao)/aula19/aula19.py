"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
'''
#         0    1    2    3    4    5
lista = ['A', 'Bacana', 'C', 'D', 10.5]
#         6     5    4    3    2    1
lista[3] = 'qualquer outra coisa.'

print(lista)
print(lista[0:3])
print(lista[::-1])
'''
"""
l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

l1.extend(l2)
print(l1)
l1.append('a')
print(l1)
l2.insert(0, 'banana')
print(l2)
l2.pop()
print(l2)

l4 = [1,2,3,4,5,6,7,8,9]

# del(l4[3:5])
print(l4)
print(max(l4))
print(min(l4))

l5 = list(range(0,100,8))
print(l5)

l6 = ['String', True, 10, -20.5]

for elem in l6:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')
"""
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você PERDEU')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'UHUUUL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFZZ: a letra "{letra}" Não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1
        print(f'Você ainda tem {chances} chances.')
        print()