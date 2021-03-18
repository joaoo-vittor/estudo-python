"""
Aula 12

Herança múltipla - Python Orientado a Objetos

"""


class A:
    def falar(self):
        print('Falando... Estou em A.')


class B(A):
    def falar(self):
        print('Falando... Estou em B.')


class C(A):
    def falar(self):
        print('Falando... Estou em C.')


# Em Herança multipla é seguido a ordem da esquerda para direita
# A class D vai procurar o metódo 'falar' primeiro em B
class D(B, C):
    pass
    # def falar(self):
    #     print('Falando... Estou em D.')


d = D()
d.falar()
