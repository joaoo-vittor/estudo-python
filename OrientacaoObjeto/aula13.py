"""
Aula 13

Classes Abstratas - Python Orientado a Objetos

"""
# abc -> abstract base class
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):  # método abstrata
        pass


class B(A):
    def falar(self):
        print('Metodo')


b = B()
b.falar()
