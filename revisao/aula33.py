"""
Aula 33

Modulos

"""

import sys
from aula33Modulos.aula33Modulo import div, soma, nomeModulo

print(sys.platform)

if __name__ == '__main__':
  print(__name__)
  print(nomeModulo())
  print(soma(1, 5))
  print(div(2, 0))
