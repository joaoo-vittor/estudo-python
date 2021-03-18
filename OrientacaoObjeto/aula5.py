"""
Aula 5

Atributos de Classe - Python Orientado a Objetos

"""

class A:
  vc = 123

a1 = A()
a2 = A()
a3 = A()

print('#'*30)

a3.vc = 321 # aqui estou criando um atribudo

print(a3.__dict__)
print(a2.__dict__)
print(a1.__dict__)
print(A.__dict__)

print('#'*30)

print('Antes de Alterar vc')

print(a1.vc)
print(a2.vc)
print(A.vc)

print('Depois de Alterar vc')

A.vc = 321

print(a1.vc)
print(a2.vc)
print(A.vc)








