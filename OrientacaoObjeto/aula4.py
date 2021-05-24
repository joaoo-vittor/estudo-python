"""
Aula 4

@property - Getters e Setters - Python Orientado a Objetos

"""

class Produto:
  def __init__(self, nome, preco):
    self.nome = nome
    self.preco = preco

  def desconto(self, percentual):
    self.preco = self.preco - (self.preco * (percentual / 100))

  # Getter
  @property
  def preco(self):
    return self.__preco

  # Setter
  @preco.setter
  def preco(self, valor):
    if isinstance(valor, str):
      valor = float(valor.replace('R$', ''))

    self.__preco = valor

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, valor):
    if isinstance(valor, str):
      self.__nome = valor.title()


p1 = Produto('CAMISETA', 50)
print(p1.nome)
p1.desconto(10)
print(p1.preco)


p2 = Produto('CANECA', 'R$16')
print(p2.nome)
p2.desconto(10)
print(p2.preco)

