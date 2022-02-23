"""
Funções aula 4 - escopo local e escopo global
"""

variavel = 'valor'

def func():
    print(variavel)

def func2():
    global variavel # declara assim pois sem global ela gera uma outra variavel com o mesmo nome e com isso afeta a variavel global
    variavel = 'Outro valor'
    print(variavel)

# uma melhor pratica para usar uma variavel dentro de uma função é
def func3(arg=None):
    arg = arg.replace('v', 'c')
    return arg

func()
func2()
outra_variavel = func3(arg = variavel)

print(variavel)
print(outra_variavel)