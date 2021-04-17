"""
Aula 6

Encapsulamento - Python Orientado a Objetos
public -> todos
protected -> na classe ou filhas da classe
private -> só na classe

-> CONVENÇÃO DO PYTHON
  _   -> protected
  __  -> private
  OBS: Tanto para Atributos quanto Métodos

"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome, sep=" -> ")

    def apaga_cliente(self, id):
        del self.__dados["clientes"][id]


bd = BaseDeDados()

bd.inserir_cliente(1, "João")
bd.inserir_cliente(2, "Vitor")
bd.inserir_cliente(3, "Otavio")

# print(bd.__dados)
bd.lista_clientes()

# bd.dados = 'alkmalksmx'

print("#" * 20)

bd.apaga_cliente(3)

bd.lista_clientes()

print("#" * 20)

# não precisa de () no getter dados
print(bd.dados)
