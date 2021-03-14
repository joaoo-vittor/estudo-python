"""
Aula 1

Classes - Python Orientado a Objetos

"""
from datetime import datetime


class Pessoa:

  ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

  def __init__(self, nome, idade, comendo=False, falando=False):
    self.nome = nome
    self.idade = idade
    self.comendo = comendo
    self.falando = falando

  def falar(self, assunto):
    if self.comendo:
      print(f'{self.nome} não pode falar comendo.')
      return
    
    if self.falando:
      print(f'{self.nome} já está falando.')
      return
    
    print(f'{self.nome} está falando de {assunto}')
    self.falando = True
  
  def parar_falar(self):
    if not self.falando:
      print(f'{self.nome} não está falando.')
      return

    print(f'{self.nome} parou de falar.')
    self.falando = False

  
  def comer(self, alimento):
    if self.comendo:
      print(f'{self.nome} já está comendo.')
      return

    if not self.falando:
      print(f'{self.nome} não pode comer falando.')
      return
    
    print(f'{self.nome} está comendo {alimento}.')
    self.comendo = True

  def parar_comer(self):
    if not self.comendo:
      print(f'{self.nome} não esta comendo.')
      return
    
    print(f'{self.nome} parou de comer.')
    self.comendo = False


p1 = Pessoa('joao', 22)
p2 = Pessoa('vitor', 25)

# print(p1)
# print(p2)
# print(p1 == p2)

print(p1.nome, '-'*12, 'data:', p1.ano_atual, '-'*12, sep=' ')
p1.comer('banana')
p1.comer('banana')

p1.falar('POO')
p1.parar_comer()

p1.falar('POO')
p1.falar('Java')

p1.parar_falar()

print('#'*30)
print(Pessoa.ano_atual)
