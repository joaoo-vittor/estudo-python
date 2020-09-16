"""
Aula 1

Introdução a Orientação a Objeto

self ->  referencia a propria instancia

"""

class Pessoa:
  def __init__(self, nome, idade, falar=False, comendo=False):
    self.nome = nome
    self.idade = idade
    self.falar = falar
    self.comendo = comendo


  #metodos
  def fala(self):
    if self.falar:
      print(f'{self.nome} esta falando...')
      return

    print(f'{self.nome} Falando ... ')
    self.falar = True


  def pararFalar(self):
    pass


  def comer(self, comida):
    pass


  def pararComer(self):
    pass



# instancias
p1 = Pessoa('nome1', 22)
p2 = Pessoa('nome2', 32)


p1.fala()
p1.fala()
p2.fala()

# print(p1)
# print(p2)



