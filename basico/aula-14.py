"""
Aula 14

or e and

"""

nome = str(input('digite seu nome: '))
idade = int(input('digite sua idade: '))

# nome = () ?  true : false

if len(nome) > 5 and idade < 18:
  print('nome tem mais de 5 letra AND é menor de idade.')
else:
  if len(nome) < 5 or idade > 18:
    print('nome tem menos de 5 letra OR é maior de idade.')
