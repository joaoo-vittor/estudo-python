"""
Aula 6

Formatação de String.

"""

nome = 'seu nome'
idade = 22
altura = 1.88
maiorIdade = idade > 18
data_atual = 2020

# Formatação de String.
print(nome, 'tem', idade, 'de idade.')
print(f'{nome} tem {idade} de idade.')
print('{0} tem {1} de idade, e {0} tem {2} de altura.'.format(nome, idade, altura))
