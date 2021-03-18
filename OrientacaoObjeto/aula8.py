"""
Aula 8

Agregação - Python Orientado a Objetos

"""
from aula8Classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 79.99)
p2 = Produto('MacBook', 7999.99)
p3 = Produto('caneta', 2.99)

produtos = [p1, p2, p3]

for prod in produtos:
    carrinho.inserir_produtos(prod)


carrinho.lista_produtos()
print(f'Total: R${carrinho.soma_total():.2f}')
