"""
Aula 28

filter

"""
from produtos import lista, pessoas, produto

# retorna o elemento que verificar em true
# nova_lista = filter(lambda item: item > 5, lista)
# print(list(nova_lista))


# Produtos maiores que 10 reais

novos_prod = filter(lambda prod: prod['preco'] > 30, produto) 

# for prodt in novos_prod:
#   print(prodt)

def filtro(pessoa):
  if pessoa['idade'] > 18:
    return True

maior_idade = filter(filtro, pessoas)

for p in maior_idade:
  print(p)

