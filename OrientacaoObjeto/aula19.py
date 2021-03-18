"""
Aula 19

Metaclasses

EM PYTHON TUDO É OBJETO: incluindo classes
Metaclasses são as "classes" que criam classes.
type é um metaclesse

"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'b_fala' not in namespace:
            print(f'Voce precisa criar o metodo b_fala {name}')

        if not callable(namespace['b_fala']):
            print(f'b_fala precisa ser metodo e não atributo em {name}')

        if 'attr_classe' in namespace:
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'valor A'

    def fala(self):
        self.b_fala()


class B(A):
    # def b_fala(self):
    #     print('Oi')

    attr_classe = 'valor B'
    b_fala = 'WoW'

    def oi(self):
        print('oi')


b = B()
# b.fala()
print(b.attr_classe)
