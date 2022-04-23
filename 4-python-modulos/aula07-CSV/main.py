"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas ( Excel, Google Sheets), base de dados, clientes de e-mail, etc...
"""
import csv

with open('./python-modulos/aula7-CSV/clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)] #reader
    # next(dados) # começa na próxima linha

    # for dado in dados:
        # print(dado['Nome'], dado['Sobrenome'], dado['E-mail'], dado['Telefone'])

with open('./python-modulos/aula7-CSV/clientes2.csv', 'w+') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )