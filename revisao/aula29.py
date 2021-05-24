"""
Aula 29

Reduce

"""

from produtos import lista, pessoas, produto
from functools import reduce

func = lambda acumulador, item: item + acumulador
soma_lista = reduce(func, lista, 0)
print(soma_lista)

func_2 = lambda acumulador, preco: preco['preco'] + acumulador
soma_total_preco = reduce(func_2, produto, 0.0)
print(f'{soma_total_preco:.2f}')
