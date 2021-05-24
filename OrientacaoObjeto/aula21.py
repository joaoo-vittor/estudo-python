"""
aula 21

Dataclasses

O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__ (etc)
em classes definidas pelo usuário.
Basicamente, dataclasses são syntax sugar para criar classes normais.
Foi originalmente descrito na PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação: https://docs.python.org/pt-br/3/library/dataclasses.html
"""

from dataclasses import dataclass
from dataclasses import field


@dataclass(eq=False, repr=False, order=False, frozen=False, init=True)
class Pessoa:
    """
    eq => implementa o metodo de igualdade
    order => Permite a ordenação de objetos de Pessoa
    frozen => Torna a classe imutavel
    init => cria o inicializador da classe
    """
    nome: str
    sobrenome: str = field(repr=False)

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise ValueError(
                f'Invalid type {type(self.nome).__name__} != str em {self}')
        # self.nome_completo = f'{self.nome} {self.sobrenome}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


p1 = Pessoa('João', 'Silva')
p2 = Pessoa('123', 'Silva')

print(p1 == p2)


# print(p1.nome)
# print(p1.sobrenome)
# print(p1.nome_completo)
