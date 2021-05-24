"""
Aula 17

Métodos mágicos - Python Orientado a Objetos

"""


class A:
    def __new__(cls, *args, **kwargs):
        # Toda classe deriva de Object
        # return super().__new__(cls)
        # print('Eu sou o new')

        # cls.nome = 'joao'

        def olaMundo(*args, **kwargs):
            print('Olá, mundo!')

        cls.olaMundo = olaMundo

        return object.__new__(cls)

    def __init__(self):
        print('Eu sou o INIT de A')


a = A()
# print(a.nome)
# a.olaMundo()

print('#'*20)


class B:
    def __new__(cls, *args, **kwargs):
        # pattern Simgolton
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = object.__new__(cls)

        return cls._jaexiste

    def __init__(self):
        print('Eu sou o INIT de B')


b = B()
c = B()

print(b == c)
print(id(b), id(c))

print('#'*20)


class C:
    def __init__(self):
        print('Eu sou o INIT de C')

    # def __call__(self, *args, **kwargs):
    #     print(args)
    #     print(kwargs)

    def __call__(self, *args, **kwargs):
        result = 0

        for i in args:
            result += i

        return result


c1 = C()
# c1(1, 2, 3, 4, 5, nome='joao')
print(c1(1, 2, 3, 4, 5))


print('#'*20)


class D:
    def __init__(self):
        print('Eu sou o INIT de D')

    def __setattr__(self, key, value):
        # print(key, value)
        self.__dict__[key] = value


d = D()
d.nome = 'joao'
print(d.nome)

print('#'*20)


class E:
    def __init__(self):
        print('Eu sou o INIT de E')

    def __del__(self):
        print('Objeto "E" coletado.')


e = E()

print('#'*20)


class F:
    def __init__(self):
        print('Eu sou o INIT de F')

    def __str__(self):
        return 'Essa é a classe "F"'


f = F()
print(f)
