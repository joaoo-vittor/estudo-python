"""
Aula 26

Groupby - Agrupando valores

"""

from itertools import groupby, tee


alunos = [
  {'nome': 'Luiz', 'nota': 'A'},
  {'nome': 'Vitor', 'nota': 'B'},
  {'nome': 'João', 'nota': 'D'},
  {'nome': 'Sophia', 'nota': 'E'},
  {'nome': 'Maria', 'nota': 'E'},
  {'nome': 'Jose', 'nota': 'F'},
  {'nome': 'Lucas', 'nota': 'A'},
  {'nome': 'Manu', 'nota': 'C'},
  {'nome': 'Sabrina', 'nota': 'C'},
  {'nome': 'Otavio', 'nota': 'B'},
]

getNota = lambda aluno: aluno['nota']

alunos.sort(key= getNota, reverse=False)
alunos_agrupados = groupby(alunos, getNota)

# print(list(alunos_agrupados))

for nota, grupo_nota in alunos_agrupados:

  # tee faz duas copias do iterador
  grupo1, grupo2 = tee(grupo_nota)

  quantidade = len(list(grupo1))
  print(f'{quantidade} Alunos com Nota: {nota}')

  for aluno_nota in grupo2:
    nome = aluno_nota['nome']
    nota = aluno_nota['nota']

    print(f'\tNome: {nome}, Nota: {nota}')

