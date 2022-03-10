
try:
    a = {}
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.', erro)
except (IndexError, KeyError) as erro:
    print('Erro de indice ou chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu código foi executado com sucesso!!!')
finally:
    print('Finalmente.')

print('Bora continuar...')