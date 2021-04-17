"""
Aula 25

Combinations, Permutations e Product - Itertools

Combinação -> Ordem não importa
Permutação -> Ordem importa
Ambos não repetem valores únicos
Produto -> Ordem imposta e repete valores únicos

"""

from itertools import combinations, permutations, product

lista_pessoas = ['Joao', 'Vitor', 'Luiz', 'Fabricio', 'Rose', 'Manu']

# Combinação
# for grupo in combinations(lista_pessoas, 2):
#   print(grupo)

# Permutação
# for grupo in permutations(lista_pessoas, 2):
#   print(grupo)

# Produto
for grupo in product(lista_pessoas, repeat=2):
  print(grupo)






