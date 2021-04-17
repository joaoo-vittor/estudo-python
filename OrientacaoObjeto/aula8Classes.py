# A classe precisa de produtos
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += float(produto.preco)
        return total


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
