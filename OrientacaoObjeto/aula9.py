"""
Aula 9

Composição - Python Orientado a Objetos

"""
from aula9Classes import Cliente, Enderecos


cliente1 = Cliente('João Vitor', 22)
print(cliente1.nome)
cliente1.insere_endereco('Campina grande', 'PB')
cliente1.lista_enderecos()
print('#'*30, end='\n\n')

cliente2 = Cliente('Maria', 37)
print(cliente2.nome)
cliente2.insere_endereco('São Paulo', 'SP')
cliente2.insere_endereco('Salvador', 'BA')
cliente2.lista_enderecos()
print('#'*30, end='\n\n')

cliente3 = Cliente('Luiz Otavio', 32)
print(cliente3.nome)
cliente3.insere_endereco('Belo Horizonte', 'MG')
cliente3.lista_enderecos()
del cliente3
print('#'*30, end='\n\n')

print('#'*10, 'GARBAGE COLLECTOR', '#'*10)
