import re

def remover_caracteres(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

def primeiro_digito(novo_cnpj):
    novo_cnpj = novo_cnpj[:-2]

    soma = 0
    lista_param = [5,4,3,2,9,8,7,6,5,4,3,2, 6,5,4,3,2,9,8,7,6,5,4,3,2]
    for indice, valor in enumerate(novo_cnpj):
        
        if indice == 12 or indice == 24:
            digito = 11 - (soma % 11)

            if digito > 9:
                digito = 0      
            soma = 0
            novo_cnpj += str(digito)

        soma += int(valor) * lista_param[indice]

    print(novo_cnpj)