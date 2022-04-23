"""
Funções (def) em python - *args **kwargs (quando não sabe a quantidade de argumentos que a função irá receber)
"""

def func(*args, **kwargs):
    print(args)
    
    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('idade não existe')


lista = [1,2,3,4,5]
lista2 = [10,40,50,80,97]
func(*lista, *lista2, nome='Leo', sobrenome='Faveri', idade='30')



