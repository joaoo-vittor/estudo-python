"""
Aula 23

Zip -> Unindo iteráveis 
 |-> só vai unir até a menor lista

Zip_longest -> itertools
  |-> vai unir elementos da maior lista e passa None para
      os que ficarem sem valor corespondente


"""

from itertools import zip_longest, count

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Campina Grande']
estados = ['SP', 'MG', 'BA']

# part 2

indice = count()
# cidades_estados = zip_longest(indice, estados, cidades, fillvalue='Estado')
cidades_estados = zip(indice, estados, cidades)

# print(list(cidades_estados))

for indice, estado, cidade in cidades_estados:
  print(indice, estado, cidade)

# part 1

# cidades_estados = zip(estados, cidades)


# print(list(cidades_estados))
# print(dict(cidades_estados))

# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))

# for i in cidades_estados:
#   print(i)

