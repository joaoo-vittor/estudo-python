"""
Aula 27

map

"""
from produtos import produto, pessoas, lista

# nova_lista = map(lambda item: item * 2, lista)
# print(nova_lista)
# print(list(nova_lista))

# ==================================

def aumenta_preco(preco):
  preco['preco'] = round(preco['preco'] * 1.05, 2)
  return preco

# precos = map(lambda prod: prod['preco'], produto)
novos_prod = map(aumenta_preco, produto)

for preco in novos_prod:
  print(preco)

