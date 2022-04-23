"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas e programas muiot leve e de fácil utilização. Muito utilizado por APIs
"""

from dados import *
import json

"""
dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave)
    print(valor)
"""

#with open('clientes.json', 'w') as arquivo:
    #json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)
