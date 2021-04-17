"""Documentação deste modulo"""

from typing import Union


x: int = 10
y: float = 10.6
z: bool = False


def funcao(p1: float, p2: str, p3: dict) -> float:
    # return p1, p2, p3
    return 10.1


# print(funcao(1.1, 'str', {}))


def funcao2() -> Union[list, dict]:
    return []


print(funcao2())
