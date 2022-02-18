"""
Manipulando strings
* String indices
* Fatiamento de strings (inicio:fim:passo)
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo

https://docs.python.org/3/Library/stdtypes.html (tipos built-in)
https://docs.python.org/3/Library/functions.html (funções built-in)
"""

# positivos [012345678]
texto     = 'Python_s2'
print(texto[2])

# negativos -[987654321]
url = 'www.google.com.br/'
print(url[:-1])

# Fatiamento
nova_string = texto
print(len(nova_string))
nova_string = texto[2:6]
print(nova_string)
nova_string = texto[:6]
print(nova_string)
nova_string = texto[7:]
print(nova_string)
nova_string = texto[0:6:2] # (inicio:fim:passo)
print(nova_string)
nova_string = texto[0::3]
print(nova_string)

for letra in texto:
    print(letra)