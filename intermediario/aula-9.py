"""
Aula 9

map

"""

pessoas = [
  {'nome': 'pessoa1', 'idade': 21},
  {'nome': 'pessoa2', 'idade': 11},
  {'nome': 'pessoa3', 'idade': 24},
  {'nome': 'pessoa4', 'idade': 67},
  {'nome': 'pessoa5', 'idade': 34},
  {'nome': 'pessoa6', 'idade': 43},
  {'nome': 'pessoa7', 'idade': 29},
  {'nome': 'pessoa8', 'idade': 18},
  {'nome': 'pessoa9', 'idade': 55},
  {'nome': 'pessoa10', 'idade': 89},
]

produtos = [
  {'produto': 'produto1', 'preco': 21.57},
  {'produto': 'produto2', 'preco': 11.00},
  {'produto': 'produto3', 'preco': 24.79},
  {'produto': 'produto4', 'preco': 67.55},
  {'produto': 'produto5', 'preco': 34.99},
  {'produto': 'produto6', 'preco': 43.25},
  {'produto': 'produto7', 'preco': 29.99},
  {'produto': 'produto8', 'preco': 18.67},
  {'produto': 'produto9', 'preco': 55.55},
  {'produto': 'produto10', 'preco': 89.89},
]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
nova_lista = map(lambda item: item * 2, lista)
print(nova_lista)
print(list(nova_lista))


precos = map(lambda prec: prec['preco'], produtos)
# print(precos)
print(list(precos))
for i in precos:
  print(i)

"""

"""
def aumenta_preco(preco):
  preco['preco'] = round(preco['preco'] * 1.05, 2)
  return preco

novos_produtos = map(lambda preco: round(preco['preco'] * 1.05, 2), produtos)
# novos_produtos = map(aumenta_preco, produtos)

for i in novos_produtos:
  print(i)
"""

# Aumente a idade de todas as pessoas em 1 ano



