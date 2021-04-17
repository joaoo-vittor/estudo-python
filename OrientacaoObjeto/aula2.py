"""
Aula 2

Métodos de classes - Python Orientado a Objetos

"""

class Pessoa:
  ano_atual = 2021

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
  def get_ano_nascimento(self):
    print(self.ano_atual - self.idade)

  @classmethod
  def por_ano_nascimento(cls, nome, ano_nascimento):
    idade = cls.ano_atual - ano_nascimento
    return cls(nome, idade)


p1 = Pessoa('joão', 22)
print(p1)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()

print('#'*30)

p2 = Pessoa.por_ano_nascimento('Vitor', 1999)
print(p2)
print(p2.nome, p2.idade)
p2.get_ano_nascimento()
