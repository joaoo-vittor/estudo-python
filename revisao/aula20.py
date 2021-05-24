"""
Aula 20

Geradores, Iteradores e Iteráveis

"""
# Iteravel
lista = [0,1,2,3,4,5]
lista = iter(lista)

# print(hasattr(lista, '__iter__'))
# print(hasattr(lista, '__next__'))

# print(next(lista))
# print(next(lista))
# print(next(lista))

import sys
import time

lista1 = list(range(1000))

# print(sys.getsizeof(lista))

def gera():
  # for i in range(100):
  #   yield i
  #   time.sleep(0.1)
  variavel = 'valor 1'
  yield variavel
  variavel = 'valor 2'
  yield variavel
  variavel = 'valor 3'
  yield variavel


g = gera()

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

l2 = [x for x in range(10000)]
print(type(l2))
print(sys.getsizeof(l2))

l3 = (x for x in range(10000))
print(type(l3))
print(sys.getsizeof(l3))



