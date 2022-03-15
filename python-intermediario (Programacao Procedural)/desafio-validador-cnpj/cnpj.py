import re
from itertools import count

def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def primeiro_digito(v1):
    v1 = v1[:-2]
    print(v1)
    soma1 = 0
    lista_param1 = [5,4,3,2,9,8,7,6,5,4,3,2]
    for indice, valor in enumerate(v1):
        mult = int(valor) * lista_param1[indice]
        soma1 += mult
        print(mult)
    print(soma1)
    digito1 = 11 - (soma1 % 11)
    if digito1 > 9:
        digito1 = '0'
    else:
        digito1 = str(digito1)
    print(digito1)