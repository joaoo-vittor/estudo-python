"""
Aula 7

split -> Divide uma String
join -> Junta uma String
enumerate -> Enumera elementos de uma lista

"""

nome = 'Um texte, outro texto'

# split retorna uma lista
listaNome = nome.split(',')

print(listaNome)


nomeJunto = ','.join(listaNome)

print(nomeJunto)

for index, valor in enumerate(nome):
  print(index, valor, nome[index])


