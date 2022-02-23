"""
Funções (def) em Python - return
"""
def divisao(n1, n2):
        if n2 == 0:
            return
        return n1/n2

variavel = divisao(8, 4)
print(variavel)

def dumb():
    return 1

var = dumb()
print(var, type(var))