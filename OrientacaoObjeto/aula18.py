from contextlib import contextmanager
"""
Aula 18

Context Manager - Criando e Usando gerenciadores de contexto

"""

"""
class Arquivo:
    def __init__(self, arquivo, modo):
        print('__init__')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('__enter__')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        self.arquivo.close()


with Arquivo('teste.txt', 'w') as f:
    f.write('Hello World!')
"""


@contextmanager
def abrir(arquivo, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('fechando arquivo')
        arquivo.close()


with abrir('teste.txt', 'w') as f:
    f.write('Ola, mundo')
