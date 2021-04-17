"""
Aula 18

List Comprehension

"""

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = [i for i in lista1]

lista3 = [i * 2 for i in lista1]
# print(lista3)


lista4 = [(x, y) for x in lista1 for y in range(3)]
# print(lista4)


tupla = (
  ('chave1', 'valor1'),
  ('chave2', 'valor2'),
)

t1 = [(x, y) for y, x in tupla]
# print(t1)

lista5 = list(range(100))
divPorDois = [i for i  in lista5 if i % 2 == 0]
# print(divPorDois)


ex1 = [i if i % 3 == 0 else 'Não é' for i in lista5]
print(ex1)

