
import sys
import os

argumentos = sys.argv
qtde_argumentos = len(argumentos)

if qtde_argumentos <= 1:
    print('faltando argumentos:')
    print('-a', 'Para listar todos os arquivos nesta pasta', sep='\t')
    print('-d', 'Para listar todos os diretórios nesta pasta', sep='\t')
    sys.exit()

so_arquivos = False
if '-a' in argumentos:
    so_arquivos = True

so_diretorios = False
if '-d' in argumentos:
    so_diretorios = True

for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)
    
    if so_diretorios:
        if os.path.isfile(arquivo):
            print(arquivo)
