"""
Aula 19

Dictionary Comprehension

"""

lista = [
  ('chave1', 'valor1'),
  ('chave2', 'valor2'),
  ('chave3', 'valor3'),
]

d1 = {x.upper(): y for x, y in lista}

print(d1)

d2 = {f'chave_{x}': x**2 for x in range(2,7)}
print(d2)

