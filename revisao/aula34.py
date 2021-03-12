"""
Aula 34

Funções decoradoras e decoradores

"""

def camada1(func):
  def camada2():
    print('Estou decorada')
    func()
  return camada2

# @<nome da função superior>
@camada1
def fala_oi():
  print('oi')

# variavel = camada1(fala_oi)
fala_oi()
