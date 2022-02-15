

nome = 'Leonardo'
idade = 30
altura = 1.85
e_maior = idade > 18
peso = 95
imc = peso / (altura**2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{1} tem {0} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))