"""
Aula 2

arg e kwarg

"""

def func(*args, **kwargs):
  print(args)

  nome = kwargs['nome']
  idade = kwargs['idade']
  print(f'{nome} tem {idade} de idade.')

arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [10, 20, 30, 40, 50]

func(*arr1, arr2, nome='seu nome', idade=22)
