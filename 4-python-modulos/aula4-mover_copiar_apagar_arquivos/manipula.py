
import os
import shutil

caminho_original = r'D:\haion\Downloads\arquivos1'
caminho_novo = r'D:\haion\Downloads\arquivos2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo): # para mover e copiar precisa ser o caminho original
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)
        
        if '.png' in file:
            os.remove(new_file_path)
            print(f'Arquivo {file} apagado com sucesso!')

        # movendo arquivos
        #shutil.move(old_file_path, new_file_path)
        #print(f'Arquivo {file} movido com sucesso!')
        #copiando arquivos
        #if '.png' in file:
            #shutil.copy(old_file_path, new_file_path)
            #print(f'Arquivo {file} copiado com sucesso!')