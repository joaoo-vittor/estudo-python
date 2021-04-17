"""
Aula 31

Levantando exceções em Python (raise)

"""

def divide_1(x, y):
  try: 
    return x/y
  except ZeroDivisionError as error:
    print('Log: ',error)
    raise 

def divide_2(x, y):
  if y == 0:
    raise ValueError("'y' não pode ser 0")
  return x / y

try:
  print(divide_2(2,0))
except ValueError as err:
  print(err)

# try:
#   print(divide(2,0))
# except ZeroDivisionError as err:
#   print(err)
