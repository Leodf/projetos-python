"""
-> É uma lista de listas de número inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados

Exercício

-> Crie uma função que encontra o primeiro duplicado considerando o segundo número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> retorne -1 (não tem duplicados)
            
            Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 4, 8, 9],
    [8, 7, 4, 6, 4, 1, 8, 7, 2, 1],
    [1, 2, 4, 3, 1, 3, 2, 8, 9, 1],
    [6, 4, 3, 1, 2, 8, 9, 5, 7, 10],
]

lista_resposta = []

def procurar_duplicado():
    for i in lista_de_listas_de_inteiros:
        print(i)
        for indice, valor in enumerate(i):
            lista_resposta.append(valor)
            print(lista_resposta)
        

procurar_duplicado()