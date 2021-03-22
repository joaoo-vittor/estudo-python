"""
aula 23

Implementando um iterator

"""


class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    def add(self, value):
        self.__items.append(value)

    def __getitem__(self, index):
        return self.__items[index]

    def __setitem__(self, index, value):
        if index >= len(self.__items):
            self.__items.append(value)
            return
        self.__items[index] = value

    def __delitem__(self, index):
        del self.__items[index]

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.__items[self.__index]
            self.__index += 1
            return item
        except IndexError:
            raise StopIteration

    def __str__(self):
        return f'{self.__class__.__name__} ({self.__items})'


if __name__ == '__main__':
    lista = MinhaLista()
    lista.add('João')
    lista.add('Vitor')

    lista[0] = 'Luiz'
    lista[2] = 'Otavio'

    print(lista[0])
    print(lista[1])
    print(lista)

    del lista[2]

    for valor in lista:
        print(valor)
