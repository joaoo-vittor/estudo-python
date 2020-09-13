"""
Aula 10

iterando string

"""

string = 'joao vitor silva'

# count = 0
# while count < len(string):
#   print(f'{string[count]}')
#   count += 1


count = 0
while count < len(string):
  if count % 2 == 0:
    aux = string[count].upper()
    print(f'{aux}' , end='')
  else:
    print(f'{string[count]}', end='')
  count += 1

print('\n')
