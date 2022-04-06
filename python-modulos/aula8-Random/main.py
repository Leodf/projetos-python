import random
import string

# inteiro = random.randint(10,20)
inteiro = random.randrange(900, 1000, 10)
# flutuante = random.uniform(10,20)
flutuante = random.random() # gera um numero aleatorio de 0 a 1

print(inteiro)
print(flutuante)

lista = ['Luiz', 'Leonardo', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
random.shuffle(lista) # embaralha a lista
print(lista)
# sorteio = random.choice(lista) # um valor
# sorteio = random.choices(lista, k=2) # pode repetir valores
sorteio = random.sample(lista, 2) # não repete valores

print(sorteio)

# gera senha aleatoria
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)