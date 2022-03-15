"""
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0,0)
print('Lendo linhas:')
print(file.read())
print('##############')

file.seek(0,0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline(), end='')

file.seek(0,0)
print(file.readlines())


file.close()
"""
# Criando o arquivo
"""
with open ('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    
"""
# Lendo o arquivo
"""
with open ('abc.txt', 'r') as file:
    print(file.read())
"""
# escrevendo no arquivo
"""
with open ('abc.txt', 'a+') as file:
    file.write('Outra linha\n')
    file.seek(0)
    print(file.read())
"""
# Apagando arquivos
import os
os.remove('abc.txt')
