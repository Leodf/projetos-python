import re

def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def primeiro_digito(cnpj_original):
    cnpj_original = cnpj_original[:-2]

    lista_param = [5,4,3,2,9,8,7,6,5,4,3,2]
    soma = sum([int(v) * lista_param[i] for i,v in enumerate(cnpj_original)])
    digito1 = 11 - (soma % 11)

    if digito1 > 9:
        digito1 = 0      

    return str (digito1)

def segundo_digito(cnpj_original):
    cnpj_original = cnpj_original[:-1]

    lista_param = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    soma = sum([int(v) * lista_param[i] for i,v in enumerate(cnpj_original)])
    digito2 = 11 - (soma % 11)

    if digito2 > 9:
        digito2 = 0      

    return str(digito2)
