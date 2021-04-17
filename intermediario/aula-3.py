"""
Aula 3

Expressões Lambda (Funções Anônimas)

"""

"""
def funcSum(a, b):
  print(a + b)


lambdaSum = lambda a, b: a + b
lambda parameter_list: expression

funcSum(2,5)
print(lambdaSum(5,33))

"""


lista = [
  ['nome1', 22],
  ['nome2', 32],
  ['nome3', 52],
  ['nome4', 12],
  ['nome5', 72],
]

def arruma(item):
  return item[1]

lista.sort(key=lambda item: item[1], reverse=False)
print(lista)

maisUm = lambda idade: idade[0][1] + 1
print(maisUm(lista))

