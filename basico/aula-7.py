"""

aula 7

input

IF, ELIF e ELSE + Booleans + Operadores Relacionais e Lógicos

Operadores Relacionais:
  > (maior que)
  < (menor que)
  >= (maior ou igual que)
  <= (menor ou igual que)
  == (igual)
  != (diferente)

  Ex:
    10 == 10 -> True
    10 != 11 -> true


Operadores Lógicos:
  and (e)
  or (ou)
  not (não)
  in (está em)
  not in (não está em)

  nome = 'seu nome'
  sInNome = 's' in nome

"""

# input recebe uma entrada do usuario
# input envolto em um int, significa que a entrada será covertida em um inteiro.
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

# if idade >= 18: -> esta verificando se a idade é maior ou igual a 18
if nome and idade >= 18:
  print(f'{nome} é menor de idade.')
elif idade >= 18:
  print('É maior de idade.')
else:
  print('É menor de idade.')


nome = 'seu nome'
sInNome = 's' in nome
aNotInNome = 'a' not in nome

print(sInNome)
print(aNotInNome)

