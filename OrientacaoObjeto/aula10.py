"""
Aula 10

Herança Simples - Python Orientado a Objetos

+-----------------------+
|  Associação - Usa     |
+-----------------------+
|  Agregação - Tem      |
+-----------------------+
|  Composição - É dono  |
+-----------------------+
|  Herança - É          |
+-----------------------+

"""
from aula10Classes import Cliente, Pessoa, Aluno

cliente1 = Cliente('joao', 22)
print(cliente1.nome)
cliente1.falar()
# O metodo comprar pertence somente a Comprar
cliente1.comprar()


aluno1 = Aluno('maria', 34)
print(aluno1.nome)
aluno1.falar()
# O metodo estudar pertence somente a Aluno
aluno1.estudar()
