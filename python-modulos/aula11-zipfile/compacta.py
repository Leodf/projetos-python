from zipfile import ZipFile
import os

caminho = r'D:\haion\Downloads\arquivos1'

with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        print(caminho_completo)