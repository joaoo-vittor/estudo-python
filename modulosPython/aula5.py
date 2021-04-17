"""
Aula 5

OS + SHUTIL - Mover, copiar e apagar arquivos

"""

import os
import shutil as sh

caminho_original = '/home/joao/Downloads/livros'
novo_caminho = '/home/joao/Downloads/livros2'

try:
    os.mkdir(novo_caminho)
except FileExistsError as e:
    print(f'Pasta {novo_caminho} já existe.')


for root, dirs, files in os.walk(caminho_original):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(novo_caminho, file)

        # sh.move(old_file_path, new_file_path)
        # sh.copy(old_file_path, new_file_path)
        # os.remove()
        print(f'Arquivo {file} movido com sucesso!')
