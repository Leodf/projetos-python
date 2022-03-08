"""
Considerando duas listas de inteiros ou floats ( lista A e lista B)
Some os valores nas listas retornando uma nova lista com valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]
=========== resultado
lista_soma = [2,4,6,8]
"""
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4,5,6,7,8,9]

lista_zip = zip(lista_a, lista_b)
lista_soma = []

for lista_a, lista_b in lista_zip:
    lista_soma.append(lista_a + lista_b)
    
print(lista_soma)






