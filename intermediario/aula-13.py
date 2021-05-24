"""
Aula 13

raise

"""

def div(num1, num2):
  try:
    return num1 / num2
  except ZeroDivisionError as error:
    print('log:',error)
    raise

try:
  div(15, 0)
except ZeroDivisionError as err:
  print(err)


def div2(n1, n2):
  if n2 == 0:
    raise ValueError('n2 não pode ser 0.')
  return n1 / n2

try:
  print(div2(15, 0))
except ValueError as error:
  print(error)
