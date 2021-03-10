"""
Aula 10

Funcao

"""

def hello(msg='Olá, ', nome='usuario'):
  print(msg, nome)

hello('Hi, ', 'joao')
hello()


def div(n1, n2):
  if not n2 <= 0:
    return n1 / n2
  return '-1'

divisao = div(10, 2)

if divisao != '-1':
  print('resultado: ', divisao)
else: 
  print('não foi possivel fazer o calculo')
