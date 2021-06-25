from typing import (Iterable, List, NewType,
                    Sequence, Union, Tuple,
                    Dict, Any, Callable)

# Primitivos
numero: int = 10
p_flutuante: float = 1.0
booleano: bool = False
string: str = 'João Vitor'

# Sequências
lista: list = [1, 2, 3]
tupla: tuple = (1, 2, 3)

# lista2: List[int] = [1, 2, 'joao']
lista2: List[int] = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'joao']
tupla2: Tuple[int, int, int, str] = (1, 2, 3, 'João')
tupla3: Tuple = (1, 2, 3, 'joao')

# Dicionário e conjunto
pessoa: Dict[str, Union[str, int]] = {'nome': 'joao vitor',
                                      'sobrenome': 'Barbosa',
                                      'idade': 23}

pessoa2: Dict[str, Any] = {'nome': 'joao vitor',
                           'sobrenome': 'Barbosa',
                           'idade': 23}

# Meu Tipo
MyDict = Dict[str, Union[str, int, List[int]]]

pessoa3: MyDict = {'nome': 'joao vitor',
                   'sobrenome': 'Barbosa',
                   'idade': 23,
                   'lista': [1, 2, 3]}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(1531321)


# Função

def retorna_funcao(func: Callable[[], None]) -> Callable:
    return func


def fala_oi() -> None:
    print('oi')


retorna_funcao(fala_oi)()

# Função soma


def retorna_funcao2(func: Callable[[int, int], int]) -> Callable:
    return func


def soma(x: int, y: int) -> int:
    return x + y


print(retorna_funcao2(soma)(10, 5))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def saudacao(self) -> None:
        print(f'Olá, {self.nome} {self.sobrenome}!!!')


def iterar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))
