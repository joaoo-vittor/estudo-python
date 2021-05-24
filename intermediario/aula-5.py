"""
Aula 5

Dicionarios

"""

d1 = {
  'chave1': 'valor1',
  'chave2': 'valor2',
  'chave3': 'valor3',
  'chave4': 'valor4',
  'chave5': 'valor5',
  'chave7': {
    'chave1': 'valor1'
  }
}

d1.update({'chave6': 'valor6'})

if d1.get('chave6') is not None:
  print(d1.get('chave6'))

d1['chave1'] = 'valorrrr'

print('')
for chave, valor in d1.items():
  print(chave, valor, sep=': ')


# print(d1['chave1'])

