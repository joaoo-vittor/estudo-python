"""
Aula 10

filter

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


nova_lista = filter(lambda x: x % 2 == 0, lista)

print(list(nova_lista))

# filtre as pessoas que são maiores que 30 anos

novas_pessoas = filter(lambda idade: idade['idade'] > 30, pessoas)
print(list(novas_pessoas))

# filter os preços maiores que R$40,00



