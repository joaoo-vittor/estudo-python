"""
Aula 7

Associação - Python Orientado a Objetos

"""
from aula7Classes import Escritor
from aula7Classes import Caneta
from aula7Classes import MaquinaDeEscrever

escritor = Escritor('João Vitor')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

print('#'*20)

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

print('#'*20)

del escritor
print(caneta.marca)
