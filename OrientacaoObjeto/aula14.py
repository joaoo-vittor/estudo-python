"""
Aula 14

Polimorfismo de sobreposição - Python Orientado a Objetos

Polimorfismo é o pricipio que permite que classes derivadas de um mesma
superclasse tenham métodos iguai (de mesma assinatura), mas comportamentos
diferentes.

Mesma Assinatura = Mesma quantidade e tipo de parâmetros

OBS: Python só suporta o polimorfismo de sobreposição
e não suporta o de Sobrecarga

"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        pass


class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()

b.fala('Um Assunto')
c.fala('Outro Assunto')
