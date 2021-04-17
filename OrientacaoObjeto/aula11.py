"""
Aula 11

Sobreposição de membros - Python Orientado a Objetos

"""
from aula11Classes import Pessoa, Cliente, ClienteVIP

c1 = Cliente('joao', 22)
c1.comprar()

print('#'*15)

c2 = ClienteVIP('Rose', 35, 'Silva')
c2.falar()
