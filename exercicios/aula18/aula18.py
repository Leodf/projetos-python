"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'
nova_string = ''

"""
for letra in texto:
    print(letra)

for numero in range(10):
    print(numero)
"""
for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)
