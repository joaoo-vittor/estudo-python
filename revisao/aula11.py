"""
Aula 11

Função

"""
def func(*args):
  return args

print(func(1, 2, 3, 4))
print(func(1, 2, 3, 4)[0])


def anotherFunc(**kwargs):
  print(kwargs)

anotherFunc(name='joao', lastName='silva')
