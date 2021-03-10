"""
Aula 15

Dicionarios

"""

"""
d1 = {
  'str': 'valor',
  123: 'Outro valor',
  (1,2,3): 'Tupla'
}

d1['novaChave'] = 'Novo valor'
d1.update({'outraNovaChave': 'outro novo valor'})

if d1.get('nomeDaChave') is not None:
  print(d1.get('nomeDaChave'))

print(d1)

print(d1.get(123))

print('\n\n')

d2 = {
  'str': 'valor',
  123: 'Outro valor',
  (1,2,3): 'Tupla'
}

print(d2)

del d2['str']

print(d2)

print(123 in d2)
print(123 in d2.keys())
print('Tupla' in d2.values())


print('\n\n')

d3 = {
  'chave1': 'valor',
  'chave2': 'Outro valor',
  'chave3': 'Tupla'
}

for key, value in d3.items():
  print(key, value)

"""

clientes = {
  'cliente1': {
    'nome': 'Otavio',
    'sobrenome': 'Miranda',
  },
  'cliente2': {
    'nome': 'João vitor',
    'sobrenome': 'Silva',
  },
}


for cli_k, cli_v in clientes.items():
  print(cli_k)
  for atrib, valores in cli_v.items():
    print(f'  {atrib} = {valores}')

print('\n\n')


d5 = { 1: 'a', 2: 'b', 3: ['c', 'd'] }
d6 = d5.copy()


d6[1] = 'João'
d6[3][0] = 'jacare'


print(d5)
print(d6)


print('\n\n')


import copy


d7 = { 1: 'a', 2: 'b', 3: ['c', 'd'] }
d8 = copy.deepcopy(d7)

d8[1] = 'João'
d8[3][0] = 'jacare'


print(d7)
print(d8)


print('\n\n')

lista = [
  ['c1', 1],
  ['c2', 2],
  ['c3', 3],
]


d9 = dict(lista)

print(d9)

d9.pop('c3')

print(d9, flush=False)


