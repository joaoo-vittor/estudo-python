"""
Aula 9

While and for

"""

"""
counter = 1
while counter <= 10:
  if counter % 2 == 0:
    print(f'{counter} é par.')
  else:
    print(f'{counter} é impar.')
  counter += 1
"""


lista = [1,2,3,4,5,6,7,8,9,10]
# for index in range(1, 11):
for enu, index in enumerate(lista):
  # print(f'{index}')
  print(f'{index} - {enu}')

