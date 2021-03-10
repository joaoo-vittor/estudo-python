"""
Aula 30

Try, Except - Tratando Exceções em Python

"""

try:
  a = {}
  print(a[12])
except NameError as error:
  print('Error:', error)
except (IndexError, KeyError) as error:
  print('Error:', error)
else:
  pass
finally:
  print('finally sempre será execultado.')

print('.....')
