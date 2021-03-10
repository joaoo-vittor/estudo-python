"""
Aula 21

Comportamento de geradores e iteradores

"""

# lista, tupla, str -> sequencia -> Iteravel

nome = 'joao vitor'
iterador = iter(nome)

print(next(iterador))
print(next(iterador))
print(next(iterador))

print('for')

for i in iterador:
  print(i)

print('Sem valores')

for valor in iterador:
  print(valor)
